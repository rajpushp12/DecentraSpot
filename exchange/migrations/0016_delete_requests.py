# Generated by Django 3.2.5 on 2021-09-16 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0015_remove_balance_usd'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Requests',
        ),
    ]
