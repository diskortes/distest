from django import forms

class EditData(forms.Form):
    name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    address = forms.CharField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea)
    email= forms.CharField(required=False)
