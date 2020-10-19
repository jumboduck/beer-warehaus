from django import forms
from .models import Producer


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'
        widgets = {'image_url': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'dark-border'
