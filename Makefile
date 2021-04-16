APP    := change
NAME   := ${APP}
TAG    := $$(git log -1 --pretty=%h) # eg 5d72e2b
SHA    := $$(git log -1 --pretty=%H) # eg 5d72e2b158be269390d4b3931ed5d0febd784fb5

# sha-${TAG} is what's being built by the custom action
# docker/build-push-action@v1.1.0
# in .github/workflows/main.yml
IMAGE  := merkely/${APP}:sha-${TAG}
LATEST := merkely/${APP}:latest

CONTAINER := ${NAME}

MERKELY_HOST = https://app.merkely.com
MERKELYPIPE = Merkelypipe.json

# all non-latest images - for prune target
IMAGES := $(shell docker image ls --format '{{.Repository}}:{{.Tag}}' $(NAME) | grep -v latest)

ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

CI_ENV_FILE := ${ROOT_DIR}/.github/merkely.env

ifeq ($(CI),true)
	# no tty on CI
	DOCKER_RUN_TTY=
	DOCKER_RUN_INTERACTIVE=
else
	# colour on terminal needs tty
	DOCKER_RUN_TTY=--tty
	# pdb needs interactive
	DOCKER_RUN_INTERACTIVE=--interactive
endif

# list the targets: from https://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile
.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

# list installed Python packages and their version numbers
pip_list:
	@docker run --rm -it --entrypoint="" ${IMAGE} pip3 list

# - - - - - - - - - - - - - - - - - - - -
# full image rebuilds, with fresh base image, and no Docker caching

rebuild: delete_base_image
	@docker build \
		--file Dockerfile \
		--no-cache \
		--tag ${IMAGE} .
	@docker tag ${IMAGE} ${LATEST}

delete_base_image:
	$(eval BASE_IMAGE = $(shell cat "${PWD}/Dockerfile" | head -n 1 | awk '{print $$2}'))
	@docker image rm ${BASE_IMAGE} 2> /dev/null || true

# - - - - - - - - - - - - - - - - - - - -

build:
	@echo ${IMAGE}
	@docker build \
		--file Dockerfile \
		--tag ${IMAGE} .
	@docker tag ${IMAGE} ${LATEST}

# - - - - - - - - - - - - - - - - - - - -
# run tests without building, by volume-mounting

define SOURCE_VOLUME_MOUNTS
	--volume ${ROOT_DIR}/source:/app/source
endef

define TESTS_VOLUME_MOUNT
    --volume ${ROOT_DIR}/tests:/app/tests
endef

# Don't add build as a dependency to test_unit.
# If you do then .github/workflows/main.yml
# will create a new docker image, overwriting the previous
# one (which was pushed to dockerhub) thus losing the digest.

test_unit:
	docker rm --force ${CONTAINER} 2> /dev/null || true
	$(eval COVERAGE_DIR = tmp/coverage/unit)
	rm -rf ${COVERAGE_DIR} && mkdir -p ${COVERAGE_DIR}
	docker run \
		--env TEST_ARG=${TEST_ARG} \
		--name ${CONTAINER} \
		${DOCKER_RUN_TTY} \
		${DOCKER_RUN_INTERACTIVE} \
		${SOURCE_VOLUME_MOUNTS} \
		${TESTS_VOLUME_MOUNT} \
	    --volume ${ROOT_DIR}/${COVERAGE_DIR}/htmlcov:/app/htmlcov \
		--entrypoint ./tests/unit/coverage_entrypoint.sh \
			${IMAGE} tests/unit/${TARGET}

pytest_help:
	@docker run \
		--entrypoint="" \
		--rm \
		${IMAGE} \
		  python3 -m pytest --help

# - - - - - - - - - - - - - - - - - - - -

DOCS_IMAGE := merkely/docs

build_docs_image:
	@docker build --tag ${DOCS_IMAGE} ${ROOT_DIR}/docs.merkely.com/

build_docs:
	@docker run \
		--rm \
		-v ${ROOT_DIR}/docs.merkely.com:/docs \
		-v ${ROOT_DIR}:/app \
		-v ${ROOT_DIR}:/docs/source/app \
		${DOCS_IMAGE} make clean html
	@cp -RP ${ROOT_DIR}/docs.merkely.com/build/html/. docs/.

refresh_doc_ref_cache:
	@docker run \
		--entrypoint="" \
		--rm \
		-v ${ROOT_DIR}:/app \
		${IMAGE} python /app/source/docs/doc_ref_cache.py

# - - - - - - - - - - - - - - - - - - - -

push:
	@docker push ${IMAGE}

pull:
	@docker pull ${IMAGE}

# Enter running container with a shell
enter:
	@docker exec -ti ${CONTAINER} sh

# Follow the container logs
follow:
	@docker container logs -f ${CONTAINER}

# Start a container with shell
shell:
	@docker run -it --rm --name ${CONTAINER} ${IMAGE} sh

# Delete all the non-latest images
prune:
	@docker image rm $(IMAGES)

# Get the repo statistics
stats:
	@echo Commits: $$(git rev-list --count master)
	@cloc .

# - - - - - - - - - - - - - - - - - - - -
# Merkely commands

merkely_declare_pipeline:
	docker run \
		--env MERKELY_COMMAND=declare_pipeline \
		--env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
		--env MERKELY_HOST=${MERKELY_HOST} \
		--env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
		--env-file ${CI_ENV_FILE} \
		--rm \
		--volume ${PWD}/${MERKELYPIPE}:/data/Merkelypipe.json \
		${LATEST}


merkely_log_artifact:
	docker run \
        --env MERKELY_COMMAND=log_artifact \
        --env MERKELY_FINGERPRINT=${MERKELY_FINGERPRINT} \
        --env MERKELY_IS_COMPLIANT=${MERKELY_IS_COMPLIANT} \
        --env MERKELY_ARTIFACT_GIT_COMMIT=${MERKELY_ARTIFACT_GIT_COMMIT} \
        --env MERKELY_ARTIFACT_GIT_URL=${MERKELY_ARTIFACT_GIT_URL} \
        --env MERKELY_CI_BUILD_NUMBER=${MERKELY_CI_BUILD_NUMBER} \
        --env MERKELY_CI_BUILD_URL=${MERKELY_CI_BUILD_URL} \
        --env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
        --env MERKELY_HOST=${MERKELY_HOST} \
        --env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
        --env-file ${CI_ENV_FILE} \
        --rm \
		--volume=${PWD}:${PWD} \
        --volume=/var/run/docker.sock:/var/run/docker.sock \
        ${LATEST}


merkely_log_evidence:
	docker run \
        --env MERKELY_COMMAND=log_evidence \
        --env MERKELY_FINGERPRINT=${MERKELY_FINGERPRINT} \
        --env MERKELY_EVIDENCE_TYPE=${MERKELY_EVIDENCE_TYPE} \
        --env MERKELY_IS_COMPLIANT=${MERKELY_IS_COMPLIANT} \
        --env MERKELY_DESCRIPTION="${MERKELY_DESCRIPTION}" \
        --env MERKELY_CI_BUILD_URL=${MERKELY_CI_BUILD_URL} \
        --env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
        --env MERKELY_HOST=${MERKELY_HOST} \
        --env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
        --env-file ${CI_ENV_FILE} \
        --rm \
        --volume=/var/run/docker.sock:/var/run/docker.sock \
        ${IMAGE}


merkely_log_test:
	docker run \
		--env MERKELY_COMMAND=log_test \
        --env MERKELY_FINGERPRINT=${MERKELY_FINGERPRINT} \
		--env MERKELY_EVIDENCE_TYPE=${MERKELY_EVIDENCE_TYPE} \
		--env MERKELY_CI_BUILD_URL=${MERKELY_CI_BUILD_URL} \
		--env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
		--env MERKELY_HOST=${MERKELY_HOST} \
		--env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
		--env-file ${CI_ENV_FILE} \
		--rm \
		--volume ${MERKELY_TEST_RESULTS_DIR}:/data/junit \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		${IMAGE}


merkely_request_approval:
	docker run \
		--env MERKELY_COMMAND=request_approval \
		--env MERKELY_FINGERPRINT="${MERKELY_FINGERPRINT}" \
		--env MERKELY_OLDEST_SRC_COMMITISH="${MERKELY_OLDEST_SRC_COMMITISH}" \
		--env MERKELY_NEWEST_SRC_COMMITISH="${MERKELY_NEWEST_SRC_COMMITISH}" \
		--env MERKELY_DESCRIPTION="${MERKELY_DESCRIPTION}" \
		--env MERKELY_SRC_REPO_ROOT="${MERKELY_SRC_REPO_ROOT}" \
		--env MERKELY_USER_DATA="${MERKELY_USER_DATA}" \
		--env MERKELY_API_TOKEN="${MERKELY_API_TOKEN}" \
		--env MERKELY_HOST="${MERKELY_HOST}" \
        --env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
        --env-file ${CI_ENV_FILE} \
		--rm \
		--volume ${PWD}:/src \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		merkely/change


merkely_approve_deployment:
	docker run \
		--env MERKELY_COMMAND=approve_deployment \
		--env MERKELY_FINGERPRINT="${MERKELY_FINGERPRINT}" \
		--env MERKELY_OLDEST_SRC_COMMITISH="${MERKELY_OLDEST_SRC_COMMITISH}" \
		--env MERKELY_NEWEST_SRC_COMMITISH="${MERKELY_NEWEST_SRC_COMMITISH}" \
		--env MERKELY_DESCRIPTION="${MERKELY_DESCRIPTION}" \
		--env MERKELY_SRC_REPO_ROOT="${MERKELY_SRC_REPO_ROOT}" \
		--env MERKELY_USER_DATA="${MERKELY_USER_DATA}" \
		--env MERKELY_API_TOKEN="${MERKELY_API_TOKEN}" \
		--env MERKELY_HOST="${MERKELY_HOST}" \
        --env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
        --env-file ${CI_ENV_FILE} \
		--rm \
		--volume ${PWD}:/src \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		merkely/change


merkely_control_deployment:
	docker run \
		--env MERKELY_COMMAND=control_deployment \
		--env MERKELY_FINGERPRINT=${MERKELY_FINGERPRINT} \
		--env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
		--env MERKELY_HOST=${MERKELY_HOST} \
		--env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
		--env-file ${CI_ENV_FILE} \
		--rm \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		merkely/change


merkely_log_deployment:
	docker run \
        --env MERKELY_COMMAND=log_deployment \
        --env MERKELY_FINGERPRINT=${MERKELY_FINGERPRINT} \
        --env MERKELY_CI_BUILD_URL=${MERKELY_CI_BUILD_URL} \
        --env MERKELY_DESCRIPTION="${MERKELY_DESCRIPTION}" \
        --env MERKELY_ENVIRONMENT=${MERKELY_ENVIRONMENT} \
        --env MERKELY_USER_DATA=${MERKELY_USER_DATA} \
        --env MERKELY_API_TOKEN=${MERKELY_API_TOKEN} \
        --env MERKELY_HOST=${MERKELY_HOST} \
        --env MERKELY_DRY_RUN=${MERKELY_DRY_RUN} \
        --env-file ${CI_ENV_FILE} \
        --rm \
        --volume=/var/run/docker.sock:/var/run/docker.sock \
        ${IMAGE}