// core js to set up functionality for stripe payments

/*---------- Variables ----------*/
var stripe_publishable_key = $('#id_stripe_publishable_key').text().slice(1, -1);
var stripe_secret_key = $('#id_stripe_secret_key').text().slice(1, -1);
// setting up by creating variables
var stripe = Stripe(stripe_publishable_key);
var elements = stripe.elements();

/*---------- Payment styling ----------*/
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

/*---------- Handling validation errors ----------*/

card.addEventListener('change', function (event) {
    var cardError = document.getElementById('card-invalid');
    if (event.error) {
        var displayError = `
        <span class="icon" role="alert">
            <i class="fas fa-exclamation-triangle"></i>
        </span>
        <span>${event.error.message}</span>`;
        $(cardError).html(displayError);
    } else {
        cardError.textContent = '';
    }
});

