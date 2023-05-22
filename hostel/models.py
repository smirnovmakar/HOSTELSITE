from django import forms
from django.db import models


class User(models.Model):
    user_name = models.CharField("ИМЯ", max_length=50)
    email = models.CharField("ПОЧТА", max_length=50)
    password = models.CharField("ПАРОЛЬ", max_length=50)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'Зарегистрированные пользователи'


class Rooms(models.Model):
    number = models.CharField("НОМЕР", max_length=2)
    today_status = models.CharField("СЕГОДНЯ", max_length=8)
    tomorrow_status = models.CharField("ЗАВТРА", max_length=8)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'номер'
        verbose_name_plural = 'Номера'