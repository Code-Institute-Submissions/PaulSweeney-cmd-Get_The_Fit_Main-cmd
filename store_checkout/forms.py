from django import forms
from .models import Order


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'email_address',
            'phone_number', 'address1', 'address2', 'town_or_city',
            'country', 'postcode', 'county',
        )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('Field is empty, please provide a first name')
        return first_name

    # removing auto labels, adding placeholders and classes

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, state or locality',
            'postcode': 'Post Code',
        }

        # setting autofocus to first and last name
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # iterating through fields and setting a requirement to be filled in
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
