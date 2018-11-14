from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from actas.forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model
# from actas.views import upload_acta_page
from datetime import datetime
from django.contrib import messages

def login_page(request):
	if request.user.is_authenticated:
		template = 'principal.html'
		return render(request, template, {})
	else:    
		template = "auth/login.html"
		form = LoginForm(request.POST)
		context = {
			'form': form
		}
		if form.is_valid():
			username = form.cleaned_data.get("Credencial")
			password = form.cleaned_data.get("Contraseña")
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login (request, user)
				return redirect('/')
			else:
				messages.error(request, 'Credencial o contraseña incorrectos')
		return render(request, template, context, messages)

def register_page(request):
	template = "auth/register.html"
	form = RegisterForm(request.POST)
	context = {
		"form": form
	}	
		
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		email = form.cleaned_data.get('email')
		# new_user = User.objects.create_user(username, email, password, is_superuser=True)
		messages.success(request, "Usuario creado correctamente")
	return render(request, template, context)

def logout_page(request):
	logout(request)
	return redirect(login_page)
