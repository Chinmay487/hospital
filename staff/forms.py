from django import forms

class Login_form(forms.Form):
    user_name = forms.CharField(max_length = 40)
    password = forms.CharField(widget = forms.PasswordInput())