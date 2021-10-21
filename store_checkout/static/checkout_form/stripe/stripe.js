// core js to set up functionality for stripe payments

/*-------------------- Variables --------------------*/
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// setting up by creating variables
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

/*-------------------- Payment Styling --------------------*/
var style = {
    base: {
        color: '#fafafa',
        fontFamily: '"Almarai", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#fafafa'
        }
    },
    invalid: {
        color: '#ba2121',
        iconColor: '#fafafa'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

/*-------------------- Handling form validations --------------------*/
card.addEventListener('change', function (event) {
    var cardError = document.getElementById('card-errors');
    if (event.error) {
        // Render an error message for the change event targeting the card-error div
        var errorMessage = 
            `<span class "icon" role="alert">
                <i class="fas fa-exclamation-triangle"></i>
            </span>
            <span>${event.error.message}</span>`;
        $(cardError).html(errorMessage);
    } else {
        cardError.textContent = '';
    }
});

/*-------------------- Form submissions --------------------*/
var formSubmit = document.getElementById('payment-form');

formSubmit.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // diabling buttons to prevent issues incase of multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // checking for the status of the save info check box
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // taken from csrf templating in the checkout form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
    // passing new information to the view
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save-info': saveInfo,
    };
    var url = '/store_checkout/cache_checkout_data/';

    // Calling the confirm payment method
    $.post(url, postData).done(function() {
            // sending card info to stripe
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(formSubmit.first_name.value),
                    name: $.trim(formSubmit.last_name.value),
                    email: $.trim(formSubmit.email_address.value),
                    address: {
                        line1: $.trim(formSubmit.address1.value),
                        line2: $.trim(formSubmit.address2.value),
                        city: $.trim(formSubmit.town_or_city.value),
                        country: $.trim(formSubmit.country.value),
                    }
                }
            },
            shipping: {
                    name: $.trim(formSubmit.first_name.value),
                    name: $.trim(formSubmit.last_name.value),
                    address: {
                        line1: $.trim(formSubmit.address1.value),
                        line2: $.trim(formSubmit.address2.value),
                        city: $.trim(formSubmit.town_or_city.value),
                        postal_code: $.trim(formSubmit.postcode.value),
                        country: $.trim(formSubmit.country.value),
                    }
                },
        // Render an error message in the event of invalid details 
        }).then(function(result) {
            if (result.error) {
                var cardError = document.getElementById('card-errors');
                var errorMessage = 
                    `<span class "icon" role="alert">
                        <i class="fas fa-exclamation-triangle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(cardError).html(errorMessage);

                // enabling buttons again so user can rectify details and try again
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);

            // submitting form in the event of updated details
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    formSubmit.submit();
                }
            }
        });
    // incase of a bad request response
    }).fail(function() {
        location.reload();
    })
});