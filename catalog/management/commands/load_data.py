
import json
from django.core.management.base import BaseCommand
from django.core.serializers import deserialize

from catalog.models import Category, Product


class Command(BaseCommand):
    """При выполнении очищает БД и заполняет ее данными из JSON файла"""
    def handle(self, *args, **kwargs):

        self.clear_db()

        data = self.read_json('./catalog.json')
        self.load_data(data)

    @staticmethod
    def clear_db() -> None:
        """Удаляет все данные из БД"""
        Category.objects.all().delete()
        Product.objects.all().delete()

    @staticmethod
    def read_json(path: str) -> dict:
        """Загрузка данных из JSON файла"""
        with open(path, encoding='utf-8') as json_file:
            return json.load(json_file)

    @staticmethod
    def load_data(data):
        """Запись данных в БД из JSON файла"""
        for obj in deserialize('json', json.dumps(data)):
            obj.save()
