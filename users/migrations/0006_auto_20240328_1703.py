# Generated by Django 3.2.19 on 2024-03-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_user_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_message',
            new_name='user_send_message',
        ),
        migrations.AddField(
            model_name='user',
            name='user_transfer_message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]