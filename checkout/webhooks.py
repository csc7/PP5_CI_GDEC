###############################################################################

"""
Webhook set up for Stripe payment events
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe

# INTERNAL:
from checkout.webhook_handler import StripeWH_Handler

###############################################################################


# Stripe DOCS, webhooks, copied and modified with Code Institue content
# on March 19th, 2022, at 16:23, from https://stripe.com/docs/webhooks

@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen webhooks from Stripe
    """

    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify the signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Error with payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Error with signature
        return HttpResponse(status=400)
    except Exception as e:
        # Other errors
        return HttpResponse(content=e, status=400)

    print("Success received webhook sent from Stripe!")

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)

    return response



#    # Handle the event
#    if event.type == 'payment_intent.succeeded':
#        payment_intent = event.data.object # contains a stripe.PaymentIntent
#        # Then define and call a method to handle the successful payment intent.
#        # handle_payment_intent_succeeded(payment_intent)
#    elif event.type == 'payment_method.attached':
#        payment_method = event.data.object # contains a stripe.PaymentMethod
#        # Then define and call a method to handle the successful attachment of a PaymentMethod.
#        # handle_payment_method_attached(payment_method)
#        # ... handle other event types
#    else:
#        print('Unhandled event type {}'.format(event.type))
#
#        return HttpResponse(status=200)