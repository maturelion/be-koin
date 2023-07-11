# Generated by Django 3.2.19 on 2023-07-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='history',
            name='tx_type',
            field=models.CharField(choices=[['send', 'send'], ['receive', 'receive']], default='send', max_length=20),
            preserve_default=False,
        ),
    ]
