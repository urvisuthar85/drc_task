from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				# user.set_password(user.password)

                # user.set_password(user.password)
				emailhere = form.cleaned_data.get('email')
				email = EmailMessage('login email ', 'hey there welcome ', to=[emailhere])
				email.send()
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')

	if request.method == 'POST':
		all_user = User.objects.all()
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if len(all_user) != 0:

			for user in all_user:
				if user.username == username:
					if user.password == password :
						data = {'username' : username,'password':password}
						return render(request,'dashboard.html',data)
			else:
				messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')




def home(request):
	return render(request, 'dashboard.html')
