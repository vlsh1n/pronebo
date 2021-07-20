# Generated by Django 3.2.4 on 2021-07-20 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210625_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Пакет')),
            ],
        ),
        migrations.AlterField(
            model_name='packprice',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.packs'),
        ),
    ]
