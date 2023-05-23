# Generated by Django 4.2.1 on 2023-05-23 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_currency_alter_wallet_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallets.currency'),
            preserve_default=False,
        ),
    ]