from django.contrib import admin

# Register your models here.
from actas.models import Acta, Ciudadano, Victimario

# class ActaAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.creador = request.user
#         obj.save()
admin.site.register(Acta)
admin.site.register(Ciudadano)
admin.site.register(Victimario)