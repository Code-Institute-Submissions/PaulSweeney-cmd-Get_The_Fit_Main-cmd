from django.http import HttpResponse


class stripeWH_Handler:
    """ Handling webhooks from stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling webhooks events"""

        return HttpResponse(
            content=f'Ths webhook has been received successfully \
                {event["type"]}', status=200)

    def handle_payment_intent(self, event):
        """ Handling a successful payment"""

        return HttpResponse(
            content=f'Ths webhook has been received successfully \
                {event["type"]}', status=200)