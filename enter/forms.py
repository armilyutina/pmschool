from django import forms


class EmailPostForms(forms.Form):
	name = forms.CharField(max_length = 100)
	school = forms.CharField(max_length=200)
	town = forms.CharField()
	email = forms.EmailField()
	phoneNumber = forms.CharField(max_length = 15)
	classNumber = forms.CharField(max_length = 30)
	