# Generated by Django 3.2.5 on 2021-09-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0011_balance_busd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('asset', models.CharField(max_length=4)),
                ('amount', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=32)),
                ('receiver', models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]
