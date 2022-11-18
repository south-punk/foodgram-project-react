"""Менеджмент-команда для наполнения базы данными."""
import json
import os

from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Tag

from backend.settings import BASE_DIR


def open_file(file_name):
    """Метод открытия файла."""
    open_file = os.path.join(os.path.join(BASE_DIR, 'data'), file_name)
    with open(open_file, mode='r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    """Класс для наполнения базы данными."""

    help = 'Наполнение базы данных из файлов ingredients.json и tags.json'

    def handle(self, *args, **kwargs):
        """Метод для наполнения базы данными."""
        for i in open_file('ingredients.json'):
            name = i['name']
            measurement_unit = i['measurement_unit']
            if not Ingredient.objects.filter(
                name=name, measurement_unit=measurement_unit
            ).exists():
                Ingredient.objects.create(
                    name=name, measurement_unit=measurement_unit
                )
            self.stdout.write(f'Ингредиент {name} внесен в базу')
        for i in open_file('tags.json'):
            name = i['name']
            color = i['color']
            slug = i['slug']
            if not Tag.objects.filter(
                name=name, color=color, slug=slug
            ).exists():
                Tag.objects.create(name=name, color=color, slug=slug)
            self.stdout.write(f'Тег {name} внесен в базу')
        self.stdout.write('Ингредиенты и теги из шаблонов внесены в базу')
