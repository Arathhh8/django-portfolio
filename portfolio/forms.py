from django import forms

class Form_contact(forms.Form):

    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()
