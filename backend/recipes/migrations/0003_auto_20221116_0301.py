# Generated by Django 3.2.16 on 2022-11-16 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=1, upload_to='recipes/images/', verbose_name='Фото блюда'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.CharField(blank=True, max_length=200, verbose_name='Единицы измерения'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Введите HEX-код цвета (Пример: #FFFAFA)', regex='^#([A-Fa-f0-9]{6})$')], verbose_name='Цвет тега в HEX'),
        ),
    ]