from django.contrib import admin
from pedidos.models import *
# Register your models here.

class clientes_admin(admin.ModelAdmin):
    list_display=("nombre","direccion",)
    search_fields=("nombre",)

class articulos_admin(admin.ModelAdmin):
    list_filter=("seccion",)

class pedidos_admin(admin.ModelAdmin):
    list_display=("numero","fecha",)
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(clientes,clientes_admin)
admin.site.register(articulos,articulos_admin)
admin.site.register(pedidos,pedidos_admin)