/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: "#1b1b1b",
        fontFamily: '"Lato", sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#aab7c4",
        },
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545",
    },
};
let card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
    let errorDiv = document.getElementById("card-errors");
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submit
let form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    card.update({ disabled: true });
    $("#submit-button").attr("disabled", true);
    $("#payment-form").fadeToggle(100);
    $("#loading-overlay").fadeToggle(100);

    let saveInfo = Boolean($("#id-save-info").attr("checked"));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        csrfmiddlewaretoken: csrfToken,
        client_secret: clientSecret,
        saveInfo: saveInfo,
    };

    let url = "/checkout/cache_checkout_data/";

    $.post(url, postData)
        .done(function () {
            stripe
                .confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: $.trim(form.company_name.value),
                            phone: $.trim(form.phone_number.value),
                            email: $.trim(form.email.value),
                            address: {
                                line1: $.trim(form.delivery_address.value),
                                line2: null,
                                country: "NO",
                                city: $.trim(form.city.value),
                                state: null,
                            },
                        },
                    },
                    shipping: {
                        name: $.trim(form.company_name.value),
                        phone: $.trim(form.phone_number.value),
                        address: {
                            line1: $.trim(form.delivery_address.value),
                            line2: null,
                            country: "NO",
                            postal_code: $.trim(form.postcode.value),
                            city: $.trim(form.city.value),
                            state: null,
                        },
                    },
                })
                .then(function (result) {
                    if (result.error) {
                        let errorDiv = document.getElementById("card-errors");
                        let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
                        $(errorDiv).html(html);
                        $("#payment-form").fadeToggle(100);
                        $("#loading-overlay").fadeToggle(100);
                        card.update({ disabled: false });
                        $("#submit-button").attr("disabled", false);
                    } else {
                        if (result.paymentIntent.status === "succeeded") {
                            form.submit();
                        }
                    }
                });
        })
        .fail(function () {
            // Reload page to show error from the view sent with django messages
            location.reload();
        });
});
