from django.contrib import admin
from .models import (
    Alimentacion, Animal, Boleto, Cliente, Empleado, Conserje,
    Cuidador, Veterinario, Diagnostico, Habitat, HistorialSalud,
    Jaula, PanelInformativo, Zoologico, Zona, Guia
)

class AnimalInline(admin.TabularInline):  # Inline para uno a muchos
    model = Animal
    extra = 1  # Número de formularios adicionales

@admin.register(Alimentacion)
class AlimentacionAdmin(admin.ModelAdmin):
    list_display = ('tipoAlimento',)
    search_fields = ('tipoAlimento',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'edad',)
    search_fields = ('nombre', 'especie',)
    list_filter = ('especie',)

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'precio',)
    list_filter = ('fecha',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('tipoHabitat',)
    search_fields = ('tipoHabitat',)

@admin.register(Zoologico)
class ZoologicoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    filter_horizontal = ('zona',)

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields =  ('nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo',)
    search_fields = ('nombre', 'cargo',)

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad',)
    search_fields = ('nombre', 'especialidad',)

admin.site.register(Conserje)
admin.site.register(Cuidador)
admin.site.register(Veterinario)
admin.site.register(Diagnostico)
admin.site.register(HistorialSalud)
admin.site.register(Jaula)
admin.site.register(PanelInformativo)
# Register your models here.
