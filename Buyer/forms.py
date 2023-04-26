from django import forms
from system.models import Order, PaymentInfo


class OrderCreateForm(forms.ModelForm):
    """ Form class for bill creation """
    class Meta:
        fields = "__all__"
        model = Order

class PaymentCreateForm(forms.ModelForm):
    """ Form class for payment creation """
    class Meta:
        fields =["credit_no"]
        model = PaymentInfo