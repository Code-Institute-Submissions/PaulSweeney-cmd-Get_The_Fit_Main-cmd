from django.http import HttpResponse


class StripeWH_Handler:
    """ Handling webhooks from stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling webhooks events"""

        return HttpResponse(
            content=f'This unhandled webhook has been received successfully \
                {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handling a successful payment intent"""

        return HttpResponse(
            content=f'This webhook has been received successfully \
                {event["type"]}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handling an unsuccessful payment"""

        return HttpResponse(
            content=f'This webhook has been received successfully \
                {event["type"]}', status=400)
