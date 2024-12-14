from django.db import models

# Create your models here.
class Zoologico(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    horarioAtencion = models.CharField(max_length=100)
    zona= models.ManyToManyField('Zona', related_name='zonas')
    empleado= models.ManyToManyField('Empleado', related_name='empleados', default=0)

    def _str_(self):
        return self.nombre + ' ' + self.direccion


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    cedula = models.CharField(max_length=10)
    numeroTelefono = models.CharField(max_length=10)

    def _str_(self):
        return self.nombre + ' ' + self.cedula


class Empleado(Persona):
    cargo = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    sueldo = models.FloatField()

    def _str_(self):
        return self.nombre + ' ' + self.cargo


class Veterinario(Empleado):
    especialidad = models.CharField(max_length=50)
    animalCargo = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre + ' ' + self.especialidad


class Guia(Empleado):
    especialidad = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='boletos_guia')

    def _str_(self):
        return self.nombre + ' ' + self.especialidad


class Cuidador(Empleado):
    areaResponsable = models.CharField(max_length=50)


class Conserje(Empleado):
    areaLimpieza = models.CharField(max_length=50)


class Taquillero(Empleado):
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='boletos_taquillero')


class Cliente(Persona):
    boleto = models.ForeignKey('Boleto', on_delete=models.CASCADE, related_name='clientes', default=0)

    def _str_(self):
        return self.nombre + ' ' + self.cedula


class Animal(models.Model):
    class TipoColumnaVertebral(models.TextChoices):
        VERTEBRADO = 'Vertebrado'
        INVERTEBRADO = 'Invertebrado'

    class TipoAlimentacion(models.TextChoices):
        CARNIVORO = 'Carnivoro'
        HERBIVORO = 'Herbivoro'
        OMNIVORO = 'Omnivoro'

    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    peso = models.FloatField()
    especie = models.CharField(max_length=50)
    historialSalud = models.CharField(max_length=50)
    tipoColumnaVertebral = models.CharField(max_length=15, choices=TipoColumnaVertebral.choices)
    tipoAlimentacion = models.CharField(max_length=15, choices=TipoAlimentacion.choices)


class Alimentacion(models.Model):
    tipoAlimento = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)


class Jaula(models.Model):
    class Estado(models.TextChoices):
        OCUPADA = 'Ocupada'
        MANTENIMIENTO = 'Mantenimiento'
        DESOCUPADA = 'Desocupada'
        RESERVADA = 'Reservada'

    codigo = models.CharField(max_length=50)
    estado = models.CharField(max_length=15, choices=Estado.choices)


class Exhibicion(models.Model):
    nombre = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre + ' ' + self.horario


class PanelInformativo(models.Model):
    nombreCientifico = models.CharField(max_length=50)
    nombreComun = models.CharField(max_length=50)
    familia = models.CharField(max_length=50)
    habitatNatural = models.CharField(max_length=50)
    dieta = models.CharField(max_length=50)
    estadoDeConservacion = models.CharField(max_length=50)


class Boleto(models.Model):
    numero = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.FloatField()


class Habitat(models.Model):
    tipoHabitat = models.CharField(max_length=100)
    temperatura = models.FloatField()
    area = models.FloatField()
    capacidad = models.CharField(max_length=100)


class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    tipoZona = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre + ' ' + self.tipoZona


class Diagnostico(models.Model):
    sintoma = models.CharField(max_length=100)
    fecha = models.DateField()


class HistorialSalud(models.Model):
    fecha = models.DateField()
    diagnostico = models.CharField(max_length=100)
    veterinario = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    anamnesis = models.CharField(max_length=100)