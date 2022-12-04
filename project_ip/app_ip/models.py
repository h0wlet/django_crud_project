from django.db import models


class University(models.Model):
    full_name = models.CharField(verbose_name='Полное название', max_length=1000)
    short_name = models.CharField(verbose_name='Краткое название', max_length=20)
    date = models.CharField(verbose_name='Дата создания', max_length=10)

    def __str__(self):
        return f'{self.short_name}'


class Student(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=100)
    date_of_birth = models.CharField(verbose_name='Дата рождения', max_length=10)
    institution = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, verbose_name='Место учебы')
    year = models.IntegerField(verbose_name='Год постуления')

    def __str__(self):
        return f'{self.name}_{self.institution}'

