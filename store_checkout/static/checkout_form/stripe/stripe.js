// core js to set up functionality for stripe payments

/*---------- Variables ----------*/
var stripePublishableKey = $('#id_stripe_publishable_key').text().slice(1, -1);
var clientSecret = $('#id_stripe_secret_key').text().slice(1, -1);
// setting up by creating variables
var stripe = Stripe(stripePublishableKey);
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
