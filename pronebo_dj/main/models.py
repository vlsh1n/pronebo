from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
