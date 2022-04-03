from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=500)
    password = forms.CharField(label='Password', max_length=250)