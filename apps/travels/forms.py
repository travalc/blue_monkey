from django import forms
import datetime

class Add_Form(forms.Form):
    destination = forms.CharField(label="Destination", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", widget=forms.TextInput(attrs={'class': 'form-control'}))
    travel_from = forms.DateField(label="Travel Date From", widget=forms.SelectDateWidget(years=range(2017, 2027), attrs={'class': 'form-control'}))
    travel_to = forms.DateField(label="Travel Date To", widget=forms.SelectDateWidget(years=range(2017, 2027), attrs={'class': 'form-control'}))