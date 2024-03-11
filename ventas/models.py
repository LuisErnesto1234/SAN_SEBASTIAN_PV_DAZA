from django.db import models

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_categoria = models.CharField(max_length=20, unique=True)
    nombre_categoria = models.CharField(max_length=100)

class Marca(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_marca = models.CharField(max_length=20, unique=True)
    nombre_marca = models.CharField(max_length=100)

class Proveedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_proveedor = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ruc_dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=20)

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_producto = models.CharField(max_length=20, unique=True)
    codigo_barras = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  
    
class Venta(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_venta = models.CharField(max_length=20, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.PositiveIntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
   
    
class Inventario(models.Model):
    codigo = models.AutoField(primary_key=True)
    stock_inicial = models.PositiveIntegerField(default=0)  
    stock_actual = models.PositiveIntegerField(default=0) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    

        
        
    
    
    
    

    

        
        
        # --- tiket ---
        
        # 2 agusas = 2 
        # 4 galletas = 4.50 
        # 1/2 arroz = 3.00
        
        
        
        # impot= 9.50 
        # metodo de pago = yape
        
        
        
        # total 
        # vendieron 
        # quedaan
        
        
        
        
        
    
    