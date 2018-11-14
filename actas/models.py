from django.db import models
import os
import random
from datetime import datetime
from django.contrib.auth import get_user_model
from actas.utils import calc_edad

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 9987899658904350980372932989787987988969879698798891237923)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext) 
	return final_filename

	# return 'detalle/{final_filename}'.format(
	# 	new_filename=new_filename,
	# 	final_filename=final_filename
	# 	)

class Acta(models.Model):
	sedes_opt = (
		('sede 1', 'sede 1'),
		('sede 2', 'sede 2'),
	)
	encabezado = models.CharField(max_length=6, choices=sedes_opt, null=True)
	motivo_inicio_proc = models.TextField(null=True)
	fecha_nac = models.DateTimeField(null=True)
	numero = models.PositiveIntegerField(null=True, unique=True)
	acta_pdf = models.ImageField(upload_to=upload_image_path,null=True)
	creador = models.ForeignKey(get_user_model(), editable=False, null=True, on_delete=models.SET_NULL)
	fecha_carga = models.DateTimeField(default=datetime.now,null=True)

	def __str__(self):
		return '%s %s %s' % (self.numero, self.creador, self.fecha_carga)

class Ciudadano(models.Model):
	nombres = models.CharField(max_length=130, null=True)
	edad = models.PositiveIntegerField(null=True)
	apellidos = models.CharField(max_length=130, null=True)
	sexo_opt = (
	('M', 'Masculino'),
	('F', 'Femenino'),
	)
	sexo = models.CharField(max_length=1, choices=sexo_opt, null=True)
	actas = models.ManyToManyField(Acta)
	ced_passport = models.PositiveIntegerField(null=True, unique=True)
	foto = models.ImageField(upload_to=upload_image_path,null=True)
	rol_opt = (
	('Victima', 'Victima'),
	('Testigo', 'Testigo'),
	)
	rol = models.CharField(max_length=7, null=True)

	def __str__(self):
		return '%s %s %s' % (self.nombres, self.apellidos, self.ced_passport)

class Victimario(models.Model):
	nombres = models.CharField(max_length=130, null=True)
	apellidos = models.CharField(max_length=130, null=True)
	acta = models.ManyToManyField(Acta)
	fecha_nac = models.DateField(null=True)
	sexo_opt = (
	('M', 'Masculino'),
	('F', 'Femenino'),
	)
	sexo = models.CharField(max_length=1, choices=sexo_opt, null=True)
	ced_passport = models.PositiveIntegerField(unique=True, null=True)
	foto = models.ImageField(upload_to=upload_image_path,null=True)
	direccion = models.TextField(null=True)
	ocupacion = models.CharField(max_length=140, null=True)

	def __str__(self):
		return '%s %s %s' % (self.nombres, self.apellidos, self.ced_passport)
