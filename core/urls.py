from django.urls import path
from .views import home, form_fichaResidente, listado_movResidente, form_movResidente, form_residente, form_stock, form_terapias, listado_residentes, listado_stock,form_del_residente,listado_fichas,form_del_fichas, form_del_terapia, form_del_MovResidente,administrador,supervisor,personal, form_stock,form_del_stock


urlpatterns = [
    path('', home, name="home"),
    path('form_fichaResidente', form_fichaResidente, name="form_dichaResidente"),
    path('form_movResidente', form_movResidente, name="form_movResidente"),
    path('form_residente', form_residente, name="form_residente"),
    path('form-del-residente/<id>', form_del_residente, name="form_del_residente"),
    path('form_stock', form_stock, name="form_stock"),
    path('form_terapias', form_terapias, name="form_terapias"),
    path('form_del_terapia/<id>', form_del_terapia, name="form_del_terapia"),  
    path('listado_residentes', listado_residentes, name="listado_residentes"),
    path('listado_stock', listado_stock, name="listado_stock"),
    path('form_fichaResidente', form_fichaResidente, name="form_fichaResidente"),
    path('listado_fichas', listado_fichas, name="listado_fichas"),
    path('form_del_fichas/<id>', form_del_fichas, name="form_del_fichas"),
    path('listado_movResidente', listado_movResidente, name="listado_movResidente"), 
    path('form_del_MovResidente/<id>', form_del_MovResidente, name="form_del_MovResidente"),
    path('supervisor', supervisor, name="supervisor"), 
    path('administrador', administrador, name="administrador"),
    path('personal', personal, name="personal"),
    path('form_stock', form_stock, name="form_stock"),
    path('form_del_stock/<id>', form_del_stock, name="form_del_stock"),
    path('listado_stock', listado_stock, name="listado_stock"),
]