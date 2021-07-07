from django.contrib import admin
from django.contrib import admin
from .models import Compra, Producto, Residente, Ficha,Terapia,TipoMovResidente, TipoProducto,MovResidente

# Register your models here.
# admin.site.register(Pais)
admin.site.register(Ficha)
admin.site.register(Residente)
admin.site.register(Terapia)
admin.site.register(TipoMovResidente)
admin.site.register(MovResidente)
admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Compra)