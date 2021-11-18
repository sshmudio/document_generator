from django import forms
from wallets.models import UserBalance


class UserBalanceForm(forms.ModelForm):
    class Meta:
        model = UserBalance
        fields = ('username', 'user_balance', 'wallet')
