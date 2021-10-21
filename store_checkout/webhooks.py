from django.conf import settings
from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from store_checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listening to Webhooks from stripe"""
    # Setting up api key and stripe webhook secret
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Extracting stripe webhook data and verify signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('success')
    return HttpResponse(status=200)


    # Handling the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object  # contains a PaymentIntent
        print('PaymentIntent was successful')

    elif event.type == 'payment_method.attached':
        payment_method = event.data.object  # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a customer')

    # Handling other event types
    else:
        return HttpResponse(status=400)

    return HttpResponse(status=200)
