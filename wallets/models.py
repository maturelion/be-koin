from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        # Create a wallet for the user
        wallet = Wallet.objects.create(user=instance)

        # Get all available currencies
        currencies = Currency.objects.all()

        # Create currency balances for each currency
        for currency in currencies:
            CurrencyBalance.objects.create(wallet=wallet, currency=currency, balance=0.0)

class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currencies = models.ManyToManyField(Currency, through='CurrencyBalance')

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class CurrencyBalance(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('wallet', 'currency')

    def __str__(self):
        return f"{self.currency.symbol} balance: {self.balance}"
