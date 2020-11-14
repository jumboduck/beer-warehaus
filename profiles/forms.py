from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_company_name': 'Company Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_delivery_address': 'Delivery Address',
            'default_postcode': 'Postal Code',
            'default_city': 'City',
        }

        self.fields['default_company_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'dark-border profile-form-input'
            self.fields[field].label = False
