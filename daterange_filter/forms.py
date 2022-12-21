from django import forms
from django.contrib.postgres.fields import DateRangeField


class MyForm(forms.Form):
    date_range = DateRangeField()
