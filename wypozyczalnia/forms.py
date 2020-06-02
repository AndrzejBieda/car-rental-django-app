from django import forms
from django.db.models import Model


class PlaceAndDate(forms.Form):
    miejsce_odb = forms.CharField()
    miejsce_zwr = forms.CharField()
    data_odb = forms.CharField()
    data_zwr = forms.CharField()


class Sam(forms.Form):
    sam = forms.CharField()


class Sam1(forms.Form):
    sam = forms.CharField()
