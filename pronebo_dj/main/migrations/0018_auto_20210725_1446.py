# Generated by Django 3.2.4 on 2021-07-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_purchase_pack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['id'], 'verbose_name': 'Вопрос/Ответ', 'verbose_name_plural': 'Вопросы/Ответы'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Фото в галерею', 'verbose_name_plural': 'Фото в галерею'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['service'], 'verbose_name': 'Фото для услуги', 'verbose_name_plural': 'Фото для услуг'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='packprice',
            options={'verbose_name': 'Стоимость пакета', 'verbose_name_plural': 'Стоимость пакетов'},
        ),
        migrations.AlterModelOptions(
            name='packs',
            options={'verbose_name': 'Пакет', 'verbose_name_plural': 'Пакеты'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['service', 'pack'], 'verbose_name': 'Услуги в пакете', 'verbose_name_plural': 'Услуги в пакетах'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['id'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='item',
            name='seo_desc',
            field=models.CharField(blank=True, max_length=255, verbose_name='SEO-описание страницы'),
        ),
        migrations.AddField(
            model_name='item',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='SEO-ключевые слова'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to='photos/gallery/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='images',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.item', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='packprice',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.packs', verbose_name='Пакет'),
        ),
        migrations.AlterField(
            model_name='packprice',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.item', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.packs', verbose_name='Пакет'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.item', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='photo',
            field=models.ImageField(upload_to='photos/clients/', verbose_name='Фото'),
        ),
    ]
