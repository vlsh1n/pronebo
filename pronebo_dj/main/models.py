from django.db import models

# Create your models here.
from django.urls import reverse


# Model for services
class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', blank=True)
    price = models.IntegerField(verbose_name='Стоимость')

    def get_absolute_url(self):
        return reverse('services', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга(-у)'
        verbose_name_plural = 'Услуг(-и)'
        ordering = ['id']


# Model for questions|answers for FAQ page
class Faq(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.CharField(max_length=1000, verbose_name='Ответ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос/Ответ'
        verbose_name_plural = 'Вопрос(-ов)/Ответ(-ов)'
        ordering = ['id']


# Model for images in service page
class Images(models.Model):
    service = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True) # Row for choosing dependence with service
    image = models.ImageField(upload_to='photos/')

    class Meta:
        ordering = ['service']


# Model for testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name='Должность/хобби')
    phrase = models.CharField(max_length=511, verbose_name='Высказывание')
    photo = models.ImageField(upload_to='photos/clients/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв(-ов)'
        ordering = ['id', 'name']
