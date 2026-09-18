from django import forms
from django.contrib.auth.forms import UserCreationForm

from InnKeeper_app.models import Login, Customer, Owner, Resorts, Facilities


class Login_form(UserCreationForm):
    class Meta:
        model = Login
        fields =('username','password1','password2')

class Customer_Form(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ('name','phone','email','address')


class Owner_Form(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name','phone','email')

class ResortForm(forms.ModelForm):
    class Meta:
        model = Resorts
        fields = ['name', 'description', 'picture', 'pricing']


class Facility_Form(forms.ModelForm):
    class Meta:
        model = Facilities
        fields ="__all__"
        exclude= ("resort",)

