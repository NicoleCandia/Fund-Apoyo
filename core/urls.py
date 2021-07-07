from django.urls import path
from .views import home, form_fichaResidente, form_login, form_movResidente, form_residente, form_stock, form_terapias, listado_residentes, listado_stock

urlpatterns = [
    path('', home, name="home"),
    path('form_fichaResidente', form_fichaResidente, name="form_dichaResidente"),
    path('form_login', form_login, name="form_login"),
    path('form_movResidente', form_movResidente, name="form_movResidente"),
    path('form_residente', form_residente, name="form_residente"),
    path('form_stock', form_stock, name="form_stock"),
    path('form_terapias', form_terapias, name="form_terapias"),
    path('listado_residentes', listado_residentes, name="listado_residentes"),
    path('listado_stock', listado_stock, name="listado_stock"),
]