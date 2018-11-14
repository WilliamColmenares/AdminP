from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from actas.models import upload_image_path, get_filename_ext, Acta, Ciudadano, Victimario

User = get_user_model()

class LoginForm(forms.Form):
	Credencial = forms.CharField(max_length=12, error_messages ={'required': 'Por favor ingrese su credencial'} , widget=forms.TextInput(
			attrs={'class': 'form-control', 'type': 'username', 'id': 'username', 'placeholder': 'Credencial', 'required': True}))
	Contraseña = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control',
			'type': 'password',
			'id': 'inputPassword',
			'placeholder': 'Contraseña',
		}))
	# def __init__(self, *args, **kwargs):
	# 	super(LoginForm, self).__init__(*args, **kwargs)


class RegisterForm(UserCreationForm):
	username = forms.CharField(label='Credencial',max_length=12)
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email')        

	# def clean_password(self):
	# 	data = self.cleaned_data
	# 	password = self.cleaned_data.get('password')
	# 	password2 = self.cleaned_data.get('password2')
	# 	if password != password2:
	# 		raise forms.ValidationError("Las contraseñas deben ser iguales.")
		# return data	

	def clean_email(self):
		email = self.cleaned_data.get('email')
		query = User.objects.filter(email=email)
		if query.exists():
			raise forms.ValidationError("El email suministrado ya existe en los registros.")
		return email	

	def clean_username(self):
		username = self.cleaned_data.get('username')
		query = User.objects.filter(username=username)
		if query.exists():
			raise forms.ValidationError("La credencial ya está registrada en el sistema.")
		return username

class Actaform(forms.Form):
	sedes_opt = (
		('sede 1', 'sede 1'),
		('sede 2', 'sede 2'),
	)
	encabezado = forms.ChoiceField(choices=sedes_opt)
	motivo_inicio_proc = forms.CharField()
	fecha_nac = forms.DateTimeField()
	numero = forms.IntegerField()
	acta_pdf = forms.ImageField()
