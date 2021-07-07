from core.forms import ResidentesForm, TerapiasForm, FichasForm, MovForm, StockForm
from django.shortcuts import render, redirect
from .models import Residente, Terapia, Ficha, MovResidente, Compra

# Create your views here.
def home(request):
    return render(request, 'core/index.html')
def form_residente(request):
    datosResidente = {
        'form' : ResidentesForm()
    }
    if request.method == 'POST':
        formulario = ResidentesForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datosResidente['mensaje'] = "Guardados correctamente"
            return redirect(to="listado_residentes")

    return render(request, 'core/form_residente.html', datosResidente)
        
        # RESIDENTE
def listado_residentes(request):
    residentes = Residente.objects.all()
    datosResidente = {"residentes": residentes}
    return render(request, 'core/listado_residentes.html', datosResidente)

def form_del_residente(request, id):
    residente = Residente.objects.get(Rut=id)
    residente.delete()
    return redirect(to="listado_residentes")
    
        # STOCK
def form_stock(request):
    datosStock = {
        'form' : StockForm()
    }
    if request.method == 'POST':
        formulario = StockForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datosStock['mensaje'] = "Guardados correctamente"
            return redirect(to="listado_stock")
            
    return render(request, 'core/form_stock.html',datosStock)
def listado_stock(request):
    compras = Compra.objects.all()
    datosCompras = {"compras": compras}
    return render(request, 'core/listado_stock.html', datosCompras)

def form_del_stock(request, id):
    compra = Compra.objects.get(idCompra=id)
    compra.delete()
    return redirect(to="listado_stock")
    
        # TERAPIAS
def form_terapias(request):
    datosTerapia = {
        'form' : TerapiasForm()
    }
    if request.method == 'POST':
        formulario = TerapiasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datosTerapia['mensaje'] = "Guardados correctamente"
            return redirect(to="listado_fichas")
            

    return render(request, 'core/form_terapias.html',datosTerapia)

def form_del_terapia(request, id):
    terapia = Terapia.objects.get(Rut=id)
    terapia.delete()

        # FICHA
def form_fichaResidente(request):
    datosFicha = {
        'form' : FichasForm()
    }
    if request.method == 'POST':
        formulario = FichasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datosFicha['mensaje'] = "Guardados correctamente"
            return redirect(to="listado_fichas")
            
    return render(request, 'core/form_fichaResidente.html',datosFicha)


def listado_fichas(request):
    fichas = Ficha.objects.all()
    datosFichas = {"fichas": fichas}
    return render(request, 'core/listado_fichas.html', datosFichas)

def form_del_fichas(request, id):
    ficha = Ficha.objects.get(Rut=id)
    ficha.delete()
    return redirect(to="listado_fichas")

        #MovResidente
def form_movResidente(request):
    datosMov = {
        'form' : MovForm()
    }
    if request.method == 'POST':
        formulario = MovForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datosMov['mensaje'] = "Guardados correctamente"
            return redirect(to="listado_movResidente")
            
    return render(request, 'core/form_movResidente.html',datosMov)

def listado_movResidente(request):
    movResidentes = MovResidente.objects.all()
    datosMov = {"movResidentes": movResidentes}
    return render(request, 'core/listado_movResidente.html', datosMov)
def form_del_MovResidente(request, id):
    movResidente = MovResidente.objects.get(idMov=id)
    movResidente.delete()
    return redirect(to="listado_movResidente")

def personal(request):
    return render(request, 'core/personal.html')

def supervisor(request):
    return render(request, 'core/supervisor.html')

def administrador(request):
    return render(request, 'core/administrador.html')
