from django.db import models

# Create your models here.


class Algorithm(models.Model):
    types = (
        ('Обменами', 'Обменами'),
        ('Выбором', 'Выбором'),
        ('Вставками', 'Вставками'),
    )

    sorts = (
        (0, 0),
        (10, 10),
        (25, 25),
        (33, 33),
        (50, 50),
        (75, 75),
        (90, 90)
    )

    item_count_c = (
        (500, 500),
        (1000, 1000),
        (2500, 2500),
        (5000, 5000)
    )

    name = models.CharField('Название', name='name', max_length=128)
    type = models.CharField('Тип', name='type', max_length=64, choices=types)
    complexity = models.CharField(
        'сложность', name='complexity', max_length=128)
    sort_percentage = models.IntegerField(
        'Процент сортировки массива', name='sort_percentage', choices=sorts)
    item_count = models.IntegerField(
        'Кол-во элементов', name='item_count', choices=item_count_c)
    time = models.FloatField('Время работы', name='time')
    iter_count = models.IntegerField('Кол-во итераций', name='iter_count')
    replacements_count = models.IntegerField(
        'Кол-во перестановок', name='replacements_count')
    code_lines_count = models.IntegerField(
        'Кол-во строк кода', name='code_lines_count')
    code = models.TextField('Код', name='code')
    # language = models.CharField('Язык', name='type', max_length=64, choices=(('Python', 'Python'), ('C++', 'C++')))
    description = models.TextField('Описание', name='description')

    class Meta:
        verbose_name = 'алгоритм сортировки'
        verbose_name_plural = 'алгоритмы сортировки'
