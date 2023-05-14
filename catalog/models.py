"""
Задание 2
В приложении каталога создайте модели:

1. Product
2. Category
и опишите для них начальные настройки.
"""
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """
        Задание 3
        Для каждой модели опишите следующие поля:

        Category
        Наименование
        Описание
    """

    category_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    # created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """
        Задание 3
        Для каждой модели опишите следующие поля:

        Product
        Наименование
        Описание
        Изображение (превью)
        Категория
        Цена за покупку
        Дата создания
        Дата последнего изменения
    """

    name_product = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    img_product = models.ImageField(upload_to='product/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def __str__(self):
        return f'{self.name_product} {self.amount}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
