from django import forms

class EditData(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)
    email= forms.CharField()
