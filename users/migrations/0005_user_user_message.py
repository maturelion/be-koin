# Generated by Django 3.2.19 on 2024-03-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_percentage_user_crypto_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
