from django.db import models

#Modelo para Residente
class Residente(models.Model):
    Rut = models.CharField(max_length=12, primary_key=True, verbose_name="Rut Residente")
    NombreResidente = models.CharField(max_length=150, verbose_name="Nombre Residente")
    Edad = models.CharField(max_length=3, null=True, blank=True, verbose_name="Edad Residente")
    NomFamiliar = models.CharField(max_length=150, null=True, blank=True, verbose_name="Nombre familiar")
    NumFamiliar = models.CharField(max_length=12, null=True, blank=True, verbose_name="Número familiar")
    # Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Residentes"
    def __str__(self):
        return self.Rut

class Terapia(models.Model):
    idTerapia = models.IntegerField(primary_key=True, verbose_name="Id de Terapia")
    NombreTerapia= models.CharField(max_length=750, verbose_name="Nombre terapia")
    DiaTerapia= models.CharField(max_length=100, verbose_name="Dia terapia")
    HoraTerapia= models.CharField(max_length=20, verbose_name="Hora terapia")
    def __str__(self):
        return self.NombreTerapia

class TipoMovResidente(models.Model):
    idTipoMovResidente = models.IntegerField(primary_key=True, verbose_name="Id del movimiento")
    TipoMovResidente= models.CharField(max_length=750, verbose_name="Nombre MovResidente")
    def __str__(self):
        return self.TipoMovResidente


class MovResidente(models.Model):
    idMov = models.IntegerField(primary_key=True, verbose_name="Id del movimiento")
    FechaMov= models.CharField(max_length=750, verbose_name="Fecha movimiento")
    HoraMov= models.CharField(max_length=750, verbose_name="Hora movimiento")
    Destino= models.CharField(max_length=750, verbose_name="Destino movimiento")
    TipoMovResidente = models.ForeignKey(TipoMovResidente, on_delete=models.CASCADE)
    Rut = models.ForeignKey(Residente, on_delete=models.CASCADE)


class Ficha(models.Model):
    Rut = models.ForeignKey(Residente, on_delete=models.CASCADE)
    Observaciones= models.CharField(max_length=750, verbose_name="Observaciones residente")
    Medicamentos= models.CharField(max_length=450, verbose_name="Medicación del residente")
    Cuidados= models.CharField(max_length=750, verbose_name="Cuidados especiales")
    Terapia = models.ForeignKey(Terapia, on_delete=models.CASCADE)
    def __str__(self):
        return self.Observaciones

class TipoProducto(models.Model):
    idTipoProducto = models.IntegerField(primary_key=True, verbose_name="Id tipo producto")
    NombreTipoProducto= models.CharField(max_length=750, verbose_name="Nombre tipo producto")
    def __str__(self):
        return self.NombreTipoProducto

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id producto")
    NombreProducto= models.CharField(max_length=750, verbose_name="Nombre producto")
    TipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    def __str__(self):
        return self.NombreProducto

class Compra(models.Model):
    idCompra = models.IntegerField(primary_key=True, verbose_name="Id compra")
    PrecioCompra= models.CharField(max_length=750, verbose_name="Precio Compra")
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    TipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    

