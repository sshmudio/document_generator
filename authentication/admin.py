from django.contrib import admin

# Register your models here.
from authentication.models import *


class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance',)


admin.site.register(UserBalance, UserBalanceAdmin)


# class BtcWalletAdmin(admin.ModelAdmin):
#     list_display = ('address', 'balance')


# admin.site.register(BtcWallet, BtcWalletAdmin)
