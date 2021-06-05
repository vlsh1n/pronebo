from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга(-у)'
        verbose_name_plural = 'Услуг(-и)'
        ordering = ['title']
