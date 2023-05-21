from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User


@receiver(post_save, sender=User)
def wallet_create(sender, instance=None, created=False, **kwargs):
    if created:
        Wallet.objects.create(user=instance, balance=0)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username
