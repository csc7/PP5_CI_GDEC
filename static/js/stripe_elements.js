/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements( // Inclusion of Google fonts based on https://stackoverflow.com/questions/44915511/stripe-elements-google-web-font-not-working, accessed on March 18th, 2022, at 6:20.
    {
        fonts: [
          {
            cssSrc: 'https://fonts.googleapis.com/css2?family=Play&display=swap',
          }
        ]
    }
);
var style = {
    base: {
        color: '#000',
        //fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontFamily: '"Play", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// End of Stripe core logic/payment flow


console.log("Stripe loaded");