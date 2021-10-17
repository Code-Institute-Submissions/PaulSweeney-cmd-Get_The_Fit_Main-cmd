from django import forms
from .models import Order


class NewOrderForm(froms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'email_address',
            'phone_number', 'address1', 'address2', 'town_or_city',
            'country', 'postcode', 'county',
        )

    # removing auto labels, adding placeholders and classes
    def __init__(*args, **kwargs):
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Post Code',
            'country': 'Country'
        }

        self.fields['first_name', 'last_name'].widget.attrs['autofocus'] = True
