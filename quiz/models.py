from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizzes'


class Quizz(models.Model):
    title = models.CharField(max_length=50, verbose_name='Quiz title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
