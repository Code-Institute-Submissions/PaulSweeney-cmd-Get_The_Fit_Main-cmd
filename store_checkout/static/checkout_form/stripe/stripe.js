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

    // sending card info to stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
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
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);

        // submitting form in the event of updated details
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                formSubmit.submit();
            }
        }
    });
});
