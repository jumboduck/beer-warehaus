from django import forms
from .models import Producer

from products.widgets import CustomClearableFileInput


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'
        widgets = {'image_url': forms.HiddenInput()}

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput(button_text="Choose Image"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'dark-border'
