from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class UserBalance(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    wallet = models.CharField(verbose_name='Wallet', max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class Transactions(models.Model):
    username = models.ForeignKey(UserBalance, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=200)

    def update(self):
        u = Transactions()


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name='Стоимость', )
    document = models.CharField(verbose_name='Док', blank=True, max_length=128)
    data = models.DateTimeField(verbose_name='Время', default=datetime.now())
    document_path = models.CharField(verbose_name='Путь к файлу', blank=True, max_length=128)
