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
    user = models.ForeignKey(UserBalance, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=200)

    def update(self):
        u = Transactions()
