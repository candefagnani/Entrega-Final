from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length = 30)
    year_of_opening = models.IntegerField()
    description = models.CharField(max_length = 100)
    leading_actor = models.CharField(max_length = 100)
    main_song = models.CharField(max_length = 100)
    song_duration = models.DecimalField(max_digits = 5, decimal_places = 2)
    publisher = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "publisher")
    imagen = models.ImageField(upload_to = "posts", null = True, blank = True)
    
    def __str__(self):
        return f"{self.id} - {self.name} ({self.year_of_opening})"

class Profile(models.Model):
    user = models.OneToOneField(to= User, on_delete = models.CASCADE, related_name = "profile")
    instagram = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    imagen = models.ImageField(upload_to = "profiles", null = True, blank = True)