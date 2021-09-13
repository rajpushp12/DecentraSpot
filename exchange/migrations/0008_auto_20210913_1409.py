# Generated by Django 3.2.5 on 2021-09-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0007_auto_20210912_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='user',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='requests',
            name='user',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='receiver',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='sender',
            field=models.CharField(max_length=32),
        ),
    ]
