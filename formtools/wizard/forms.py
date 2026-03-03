from django import forms
from django.core.exceptions import ValidationError


class ManagementForm(forms.Form):
    """
    ``ManagementForm`` is used to keep track of the current wizard step.
    """

    template_name = "django/forms/p.html"  # Remove when Django 5.0 is minimal version.
    current_step = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self.steps = kwargs.pop("steps", None)
        super().__init__(*args, **kwargs)

    def clean_current_step(self):
        value = self.cleaned_data["current_step"]
        if value not in self.steps:
            raise ValidationError("Invalid step name.")
        return value
