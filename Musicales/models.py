from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    musical = models.CharField(max_length = 30)
    estreno = models.IntegerField()
    descripcion = models.CharField(max_length = 2000)
    actor_principal = models.CharField(max_length = 100)
    cancion_principal = models.CharField(max_length = 100)
    duracion = models.DecimalField(max_digits = 5, decimal_places = 2)
    publisher = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "publisher")
    imagen = models.ImageField(upload_to = "posts", null = True, blank = True)
    puntuacion = models.IntegerField(choices=((1, "1 estrella"), (2, "2 estrellas"), (3, "3 estrellas"), (4, "4 estrellas"), (5, "5 estrellas")), null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add = True)
    comentario = models.CharField(max_length = 2000)
    

    def __str__(self):
        return f"{self.id} - {self.musical} ({self.estreno})"

    def calificar(self, puntuacion):
        if self.puntuacion is not None:
            self.puntuacion = round((self.puntuacion + puntuacion) / 2, 1)
        else:
            self.puntuacion = puntuacion
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(to = User, on_delete = models.CASCADE, related_name = "profile")
    instagram = models.CharField(max_length = 100)
    email = models.EmailField()
    imagen = models.ImageField(default = 'default.png', upload_to = 'profiles')

    def __str__(self):
        return f"Usuario: {self.user} - Instagram: {self.instagram}"

class Mensaje(models.Model):
    mensaje = models.TextField(max_length = 1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "destinatario")