from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ('company_name', 'email',
                  'phone_number', 'delivery_address',
                  'postcode', 'city',)

    def __init__(self, *args, **kwargs):
        """
        # When initializing the form, add placeholders and classes,
        # remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'delivery_address': 'Delivery Address',
            'postcode': 'Postal Code',
            'city': 'City',
        }

        self.fields['company_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
