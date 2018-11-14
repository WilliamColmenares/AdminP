import datetime

def calc_edad(valor):
	dob = valor.fecha_nac
	tod = datetime.date.today()
	edad = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
	return edad