from django.contrib import admin
from django.contrib import admin
from .models import Residente, Ficha,Pais,Terapia

# Register your models here.
# admin.site.register(Pais)
admin.site.register(Ficha)
admin.site.register(Residente)
admin.site.register(Terapia)

