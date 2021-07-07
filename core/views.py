from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')
def form_fichaResidente(request):
    return render(request, 'core/form_fichaResidente.html')
def form_login(request):
    return render(request, 'core/form_login.html')
def form_movResidente(request):
    return render(request, 'core/form_movResidente.html')
def form_residente(request):
    return render(request, 'core/form_residente.html')
def form_stock(request):
    return render(request, 'core/form_stock.html')
def form_terapias(request):
    return render(request, 'core/form_terapias.html')
def listado_residentes(request):
    return render(request, 'core/listado_residentes.html')
def listado_stock(request):
    return render(request, 'core/listado_stock.html')  