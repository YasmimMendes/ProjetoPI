from django.contrib import admin;
from hospedagem.models import *;

# Register your models here.
class EstadiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente');

class Tipo_QuartoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao');

admin.site.register(Tipo_Quarto, Tipo_QuartoAdmin);
admin.site.register(Estadia, EstadiaAdmin);
