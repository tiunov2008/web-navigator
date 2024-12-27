from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    userScore = models.FloatField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ]) 
    def __str__(self):
        return self.user.username
    