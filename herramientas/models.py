from django.db import models

class Nota(models.Model):
    id_estudiante = models.IntegerField() 
    nombre = models.CharField(max_length=10) 
    nota = models.IntegerField()  
    creditos = models.IntegerField() 

    def __str__(self):
        return f"{self.nombre} - Nota: {self.nota}"
