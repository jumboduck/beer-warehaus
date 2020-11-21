from django import forms
from .models import Slide

from products.widgets import CustomClearableFileInput


class SlideForm(forms.ModelForm):

    class Meta:
        model = Slide
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'dark-border'
