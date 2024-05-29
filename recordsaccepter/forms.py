from django import forms

class Records(forms.Form):
    id = forms.CharField(label="issuer id", max_length=100)
    name = forms.CharField(label="issuer name", max_length=100)
    description = forms.CharField(label="record description", max_length=100)
    date = forms.DateField(label="issue date")
