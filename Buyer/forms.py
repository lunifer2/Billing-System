from django import forms
from system.models import Order


class OrderCreateForm(forms.ModelForm):
    """ Form class for bill creation """
    class Meta:
        fields = "__all__"
        model = Order