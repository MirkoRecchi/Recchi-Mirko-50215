from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

#-------------------PanelDeAdministracion-----------------------------

admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Examen)
admin.site.register(Calificacion)
admin.site.register(Cursado)
admin.site.register(Mesa)
admin.site.register(Comision)
admin.site.register(Permission)
admin.site.register(Modelo)