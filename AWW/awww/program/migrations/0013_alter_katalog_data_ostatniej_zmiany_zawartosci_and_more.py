# Generated by Django 4.1.7 on 2023-05-03 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0012_plik_tresc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 14, 18, 519411)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 14, 18, 519386)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 14, 18, 519403)),
        ),
    ]
