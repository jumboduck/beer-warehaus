from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')

    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'

    # Overwrite the init method to accept button text  as an argument
    def __init__(self, *args, **kwargs):
        super().__init__()

    # Overwrite the get_context method to send button_text to the template
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        return context
