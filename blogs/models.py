from django.db import models
from django.urls import reverse

'''
Задание 2
Создайте новую модель блоговой записи со следующими полями:

заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
'''


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок статьи')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    description = models.TextField(verbose_name='содержимое')
    img_blog = models.ImageField(upload_to='blogs/', verbose_name='Аватарка', null=True, blank=True)
    create_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:view', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
