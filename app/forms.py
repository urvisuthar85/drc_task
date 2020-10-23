from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
# from django.contrib.auth.models import User


class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','phone','password']
