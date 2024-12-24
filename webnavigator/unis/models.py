from django.db import models

# Create your models here.
class Uni(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    data = models.DateTimeField(auto_now_add=True)