from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    #implementacion del metodo _str_que nos devolvera una representacion de una cadena de un objeto 
    # En este caso la estamos usando porque queremos ver el titulo del nombre de la tarea en el panel
    def __str__(self):
           return self.title
