from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Style


class ProductForm(forms.ModelForm):
    """
    # This form is used for adding a new product to the store
    # or editing an existing product.
    """

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'image_url': forms.HiddenInput()}

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        styles = Style.objects.all().order_by('name')
        friendly_names = [(s.id, s.get_friendly_name()) for s in styles]

        self.fields['style'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'dark-border'
