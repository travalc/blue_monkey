from django import forms

class Registration_Form(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label="Birthday", widget=forms.SelectDateWidget(years=range(1920, 2016), attrs={'class': 'form-control'}))

class Login_Form(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))