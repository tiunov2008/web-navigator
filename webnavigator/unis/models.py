from django.db import models

# Create your models here.
class Uni(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    wage = models.IntegerField()
    source = models.URLField(null=True)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    