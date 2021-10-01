from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class Order_Form(ModelForm):
    class Meta:
        model = Order
        fields ="__all__"
class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields ="__all__"
        exclude = ['user'  ]
class Announce_Form(ModelForm):
    class Meta:
        model = Announcement
        fields ="__all__"
        exclude = ['user','customer'  ]
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']