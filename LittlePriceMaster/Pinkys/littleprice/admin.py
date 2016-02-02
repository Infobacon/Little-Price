from django.contrib import admin

# Register your models here.


from littleprice.models import *
admin.site.register(Producto)
admin.site.register(ProductoPrecio) 
admin.site.register(Reporte) 
admin.site.register(Supermercado)
admin.site.register(Usuario)
admin.site.register(Valoracion)




