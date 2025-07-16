from django.db import models

class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]
    
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
        ('En_tratamiento', 'En tratamiento'),
        ('Reservado', 'Reservado'),
    ]
    
    id_masc = models.AutoField(primary_key=True)
    nombre_masc = models.CharField(max_length=100, verbose_name="Nombre")
    especie = models.CharField(max_length=50, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100, blank=True, null=True)
    edad_masc = models.PositiveIntegerField(verbose_name="Edad")
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Disponible')
    descripcion = models.TextField(blank=True, null=True)
    foto_masc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_masc} ({self.especie})"

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

class Fundacion(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    # Agrega otros campos necesarios

    def __str__(self):
        return self.nombre