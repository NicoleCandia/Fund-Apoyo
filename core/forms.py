from django.forms import ModelForm
from .models import Compra, Residente, Terapia, Ficha, MovResidente, Compra

class ResidentesForm(ModelForm):
    class Meta:
        model = Residente
        fields = ['Rut', 'NombreResidente', 'Edad', 'NomFamiliar', 'NumFamiliar']

class TerapiasForm(ModelForm):
    class Meta:
        model = Terapia
        fields = ['idTerapia', 'NombreTerapia', 'DiaTerapia', 'HoraTerapia']

class FichasForm(ModelForm):
    class Meta:
        model = Ficha
        fields = ['Rut', 'Observaciones', 'Medicamentos', 'Cuidados', 'Terapia']

class MovForm(ModelForm):
    class Meta:
        model = MovResidente
        fields = ['idMov', 'FechaMov', 'HoraMov', 'Destino', 'TipoMovResidente','Rut']
class StockForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['idCompra', 'PrecioCompra', 'Producto', 'TipoProducto']