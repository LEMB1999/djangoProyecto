from django.db import models

# Create your models here.
class Pelicula(models.Model):
    title = models.CharField(max_length=25)
    url_img = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title