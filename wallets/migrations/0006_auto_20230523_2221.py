# Generated by Django 3.2.19 on 2023-05-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0005_alter_currencybalance_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencybalance',
            options={'ordering': ['-balance']},
        ),
        migrations.AddField(
            model_name='currency',
            name='icon',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
