from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.now, auto_created=True)
    balance = models.FloatField(verbose_name='Balance', default=0)

class BtcWallet(models.Model):
    address = models.CharField(
        verbose_name='BTC Wallet', max_length=100, unique=True)
    balance = models.DecimalField(
        verbose_name='Balance', decimal_places=8, default=0, max_digits=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = 'BTC wallets'
        verbose_name_plural = 'BTC wallets'

