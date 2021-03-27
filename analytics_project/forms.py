from django import forms
from .models import Country

class CountryData(forms.Form):
	class meta:
		model = Country
		fields = '__all__'