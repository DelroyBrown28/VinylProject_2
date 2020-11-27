from django.contrib.auth import get_user_model
from django import forms
from .models import FormatVariation, OrderItem, Product, Address


User = get_user_model()


class AddToCartForm(forms.ModelForm):
    format = forms.ModelChoiceField(queryset=FormatVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'format']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['format'].queryset = product.available_formats.all()

# Collects address from User and stores to profile
class AddressForm(forms.Form):
    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    street_name_and_number = forms.CharField(required=False)
    town_or_city = forms.CharField(required=False)
    county = forms.CharField(required=False)
    postcode = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        # user = User.objects.get(id=user_id)

        shipping_address_queryset = Address.objects.filter(
            # user=user,
            address_type='S'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_queryset

    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('street_name_and_number', None):
                self.add_error("street_name_and_number",
                               "Please fill in this field")
            if not data.get('town_or_city', None):
                self.add_error("town_or_city", "Please fill in this field")
            if not data.get('county', None):
                self.add_error("county", "Please fill in this field")
            if not data.get('postcode', None):
                self.add_error("postcode", "Please fill in this field")

