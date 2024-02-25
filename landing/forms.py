from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Custom Contact Form
    """

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={"data-theme": "dark"}))

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
