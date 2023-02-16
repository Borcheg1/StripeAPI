from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
