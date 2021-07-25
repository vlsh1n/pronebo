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
    users = models.IntegerField(verbose_name='Количество участников')
    place = models.CharField(max_length=255, verbose_name='Место')
    program = models.TextField(blank=True, verbose_name='Программа')
    restrictions = models.TextField(blank=True, verbose_name='Ограничения')
    seo_desc = models.CharField(max_length=255, blank=True, verbose_name='SEO-описание страницы')
    seo_keywords = models.CharField(max_length=1000, blank=True, null=True, verbose_name='SEO-ключевые слова')

    def get_absolute_url(self):
        return reverse('services', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
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
        verbose_name_plural = 'Вопросы/Ответы'
        ordering = ['id']


# Model for images in service page
class Images(models.Model):
    service = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True, verbose_name='Услуга')
    image = models.ImageField(upload_to='photos/', verbose_name='Фото')

    class Meta:
        ordering = ['service']
        verbose_name = 'Фото для услуги'
        verbose_name_plural = 'Фото для услуг'


# Model for testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name='Должность/хобби')
    phrase = models.TextField(max_length=511, verbose_name='Высказывание')
    photo = models.ImageField(upload_to='photos/clients/', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']


class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/gallery/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото в галерею'
        verbose_name_plural = 'Фото в галерею'


class Purchase(models.Model):
    service = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True, verbose_name='Услуга')
    pack = models.ForeignKey('Packs', on_delete=models.SET_NULL, null=True, verbose_name='Пакет')
    title = models.CharField(max_length=255, verbose_name='Название')
    allow = models.BooleanField(verbose_name='Доступность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги в пакете'
        verbose_name_plural = 'Услуги в пакетах'
        ordering = ['service', 'pack']


class PackPrice(models.Model):
    service = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True, verbose_name='Услуга')
    pack = models.ForeignKey('Packs', on_delete=models.SET_NULL, null=True, verbose_name='Пакет')
    price = models.IntegerField(verbose_name='Стоимость')

    # def __str__(self):
    #     return str(self.service)

    class Meta:
        verbose_name = 'Стоимость пакета'
        verbose_name_plural = 'Стоимость пакетов'


class Packs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Пакет')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'

