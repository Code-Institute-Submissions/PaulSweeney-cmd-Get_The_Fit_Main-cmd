from django import forms
from .models import Review, Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["sku", "name", "detail_01", "detail_02", "detail_03", "price", "rating", "image_url"]

    def clean(self):
        super(ProductForm, self).clean()

        sku = self.cleaned_data.get('sku')
        name = self.cleaned_data.get('name')
        detail_01 = self.cleaned_data.get('detail_01')
        detail_02 = self.cleaned_data.get('detail_02')
        detail_03 = self.cleaned_data.get('detail_03')
        price = self.cleaned_data.get('price')
        rating = self.cleaned_data.get('rating')
        image_url = self.cleaned_data.get('image_url')

        if len(sku) < 9:
            self._errors['sku'] = self.error_class([
                'Minimum of 9 characters required'
            ])
        if len(name) < 20:
            self._errors['name'] = self.error_class([
                'Minimum of 20 characters required'
            ])
        if len(detail_01) < 10:
            self._errors['detail_01'] = self.error_class([
                'Detail must be a minumum of 100 charactrs long \
                and 1000 characters long including letters only'
            ])
        if len(detail_02) < 10:
            self._errors['detail_02'] = self.error_class([
                'Detail must be a minumum of 100 characters \
                long and 1000 characters long including letters only'
            ])
        if len(detail_03) < 10:
            self._errors['detail_03'] = self.error_class([
                'Detail must be a minumum of 100 characters \
                long and 1000 characters long including letters only'
            ])
        if len(price) < 6:
            self._errors['price'] = self.error_class([
                'Price must be a maximum of 6 numbers and \
                please include a decimal point i.e "52.99"'
            ])
        if len(rating) < 6:
            self._errors['detail_01'] = self.error_class([
                'Rating cannot be left blank, please make \
                sure you include numbers only \
                include a decimal point i.e "4.5"'
            ])
        if len(image_url) < 6:
            self._errors['detail_01'] = self.error_class([
                "Please include the entire URL including https://"
            ])

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
