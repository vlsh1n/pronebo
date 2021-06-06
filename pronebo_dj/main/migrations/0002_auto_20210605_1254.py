# Generated by Django 3.2.4 on 2021-06-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['title'], 'verbose_name': 'Услуга(-у)', 'verbose_name_plural': 'Услуг(-и)'},
        ),
        migrations.AlterField(
            model_name='item',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
