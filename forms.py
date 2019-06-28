from django import forms
from uform.models import Userform
from phonenumber_field.formfields import PhoneNumberField
class Userformdd(forms.Form):
    email = forms.EmailField(max_length=100, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(max_length=100, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    dob = forms.CharField(max_length=100, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date'}))
    mobileno = PhoneNumberField(max_length=100, help_text='Required', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type':'tel','placeholder': 'Phone no'}))
