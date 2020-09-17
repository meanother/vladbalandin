from django.db import models
from datetime import datetime


# Create your models here.
# message_dt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')


class ShortQuestions(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    message = models.CharField(max_length=4096, verbose_name='Текст сообщения')
    email = models.EmailField(blank=True, default=None, null=True, verbose_name='Эл. почта')
    is_processed = models.CharField(max_length=255, default='N', verbose_name='Статус процесса')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'dt_short'


class PollQuestions(models.Model):
    summ = models.CharField(max_length=510, verbose_name='Общая сумма задолженности')
    amount = models.CharField(max_length=255, verbose_name='Кол-во кредиторов')
    income = models.CharField(max_length=510, verbose_name='Ежемесячный доход')
    pledge = models.CharField(max_length=255, verbose_name='Ипотека или иное имущество')
    property = models.CharField(max_length=4000, verbose_name='Владение имуществом')
    city = models.CharField(max_length=510, verbose_name='Город')
    email = models.EmailField(blank=True, default=None, null=True, verbose_name='Эл. почта')
    registration_city = models.CharField(max_length=510, verbose_name='Город регистрации')
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=500, verbose_name='Номер телефона')
    is_processed = models.CharField(max_length=255, default='N', verbose_name='Статус процесса')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'dt_poll_questions'


class QuizQuestions(models.Model):
    sum = models.CharField(max_length=510, verbose_name='Общая сумма задолженности')
    amount = models.CharField(max_length=255, verbose_name='Кол-во кредиторов')
    has_delay = models.CharField(max_length=255, verbose_name='Просрочка по платежам')
    income = models.CharField(max_length=510, verbose_name='Оф. доход')
    has_child = models.CharField(max_length=255, verbose_name='Дети')
    is_marriage = models.CharField(max_length=255, verbose_name='Брак')
    property = models.CharField(max_length=4000, verbose_name='Собственность')
    own_per_marriage = models.CharField(max_length=255, verbose_name='Собственность, приобретенаня в браке')
    property_transaction = models.CharField(max_length=255, verbose_name='Сделки с имуществом')
    pledge = models.CharField(max_length=255, verbose_name='Ипотека или залог')
    name = models.CharField(max_length=255, verbose_name='Имя')
    city = models.CharField(max_length=510, verbose_name='Город')
    phone_number = models.CharField(max_length=500, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, default=None, null=True, verbose_name='Эл. почта')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'dt_quiz_questions'



