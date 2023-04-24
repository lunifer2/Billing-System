from django import forms
from .models import Bill, PaymentInfo, Order, Item, CustomUser

class PaymentInfoCreateForm(forms.ModelForm):
    """ Form class for payment info """
    class Meta:
        fields = "__all__"
        model = PaymentInfo

class BuyerCreateForm(forms.ModelForm):
    """ Form class for buyer creation """
    class Meta:
        fields = ['first_name','last_name','username','password' ,'contact', 'email', 'address', 'gender', 'role']
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(attrs={'input_type': 'password'}),
            'contact': forms.NumberInput(attrs={'input_type': 'number'}),
        }
        
class SellerCreateForm(forms.ModelForm):
    """ Form class for seller creation """
    class Meta:
        fields = ['first_name','last_name','username','password' ,'contact', 'email', 'address', 'gender', 'role']
        model = CustomUser
        widgets = {
            'password': forms.PasswordInput(attrs={'input_type': 'password'}),
            'contact': forms.NumberInput(attrs={'input_type': 'number'}),
        }

class OrderCreateForm(forms.ModelForm):
    """ Form class for Order creation """
    class Meta:
        fields = "__all__"
        model = Order

class BillCreateForm(forms.ModelForm):
    """ Form class for bill creation """
    class Meta:
        fields = "__all__"
        model = Bill

class ItemCreateForm(forms.ModelForm):
    """ Form class for item creation """
    class Meta:
        fields = "__all__"
        model = Item                                