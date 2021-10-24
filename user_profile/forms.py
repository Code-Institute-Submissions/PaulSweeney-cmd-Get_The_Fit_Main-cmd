from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    # removing auto labels, adding placeholders and classes
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_address1': 'Address 1',
            'default_address2': 'Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, state or locality',
            'default_postcode': 'Post Code',
            'default_country': 'Country',
        }

        # setting autofocus to default
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # iterating through fields and setting a requirement to be filled in
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-white rounded-0 profile-form-input'
                self.fields[field].label = False
