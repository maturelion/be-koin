from django.db import models
from users.models import User
from wallets.models import Currency

TX_TYPE = [
    ["send", "send"],
    ["receive", "receive"],
]


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tx_type = models.CharField(choices=TX_TYPE, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
