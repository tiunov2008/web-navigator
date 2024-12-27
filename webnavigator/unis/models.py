from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Uni(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    about = models.TextField()
    wage = models.IntegerField()
    source = models.URLField(null=True)
    slug = models.SlugField()
    img = models.ImageField(default='empty.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    scoreBudget = models.FloatField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ]) 
    scorePaid = models.FloatField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ]) 
    def __str__(self):
        return self.title
