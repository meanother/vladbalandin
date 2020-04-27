from django.db import models


# Create your models here.


class ShortQuestions(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.CharField(max_length=4096)
    email = models.EmailField(blank=True, default=None, null=True)
    is_processed = models.CharField(max_length=255, default='N')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dt_short'


class PollQuestions(models.Model):
    summ = models.CharField(max_length=510)
    amount = models.CharField(max_length=255)
    income = models.CharField(max_length=510)
    pledge = models.CharField(max_length=255)
    property = models.CharField(max_length=4000)
    city = models.CharField(max_length=510)
    email = models.EmailField(blank=True, default=None, null=True)
    registration_city = models.CharField(max_length=510)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=500)
    is_processed = models.CharField(max_length=255, default='N')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dt_poll_questions'
