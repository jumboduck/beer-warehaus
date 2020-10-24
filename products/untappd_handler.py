from django.conf import settings

import requests


class UntappdHandler:

    def __init__(self, request):
        self.request = request

    def search_producer(query):
        # Build url from request
        url = f'https://api.untappd.com/v4/search/brewery?q={query}&client_id={settings.UNTAPPD_CLIENT_ID}&client_secret={settings.UNTAPPD_SECRET}'
        response = requests.get(url)

        # Catch errors
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        # Keep only the items for the response
        brewery_list = response.json()['response']['brewery']['items']

        # Return the 5 first results
        return brewery_list[:5]

    def get_producer_info(id):
        # Build url from request
        url = f'https://api.untappd.com/v4/brewery/info/{id}?client_id={settings.UNTAPPD_CLIENT_ID}&client_secret={settings.UNTAPPD_SECRET}'
        response = requests.get(url)
        
        # Catch errors
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
        
        producer_info = response.json()['response']['brewery']

        return producer_info

    def search_beer(query):
        # Build url from request https://api.untappd.com/v4/search/beer?q=Pliny
        url = f'https://api.untappd.com/v4/search/beer?q={query}&client_id={settings.UNTAPPD_CLIENT_ID}&client_secret={settings.UNTAPPD_SECRET}'
        response = requests.get(url)

        # Catch errors
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        # Keep only items in the response
        beer_list = response.json()['response']['beers']['items']

        # Return the 10 first results
        return beer_list[:10]

    def get_beer_info(id):
        # Build url from request
        url = f'https://api.untappd.com/v4/beer/info/{id}?client_id={settings.UNTAPPD_CLIENT_ID}&client_secret={settings.UNTAPPD_SECRET}'
        response = requests.get(url)

        # Catch errors
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        beer_info = response.json()['response']['beer']

        return beer_info
