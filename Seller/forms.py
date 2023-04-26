from django import forms
from system.models import Bill, Item


class BillCreateForm(forms.ModelForm):
    """ Form class for bill creation """
    class Meta:
        fields = "__all__"
        model = Bill

class ItemCreateForm(forms.ModelForm):
    """ Form class for item creation """
    class Meta:
        fields = ["item_name", "item_description", "item_image", "item_price"]
        model = Item