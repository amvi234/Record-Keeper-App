import datetime
from django import forms


class Records(forms.Form):
    id = forms.CharField(label="issuer id", max_length=100, required=True)
    name = forms.CharField(label="issuer name", max_length=100, required=True)
    description = forms.CharField(label="record description", max_length=100)
    date = forms.DateField(
        initial=datetime.date.today, label="issue date", required=True
    )
