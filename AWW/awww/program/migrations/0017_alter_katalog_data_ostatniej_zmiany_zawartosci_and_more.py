# Generated by Django 4.1.7 on 2023-05-03 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0016_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 52, 37, 49072)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 52, 37, 49048)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 52, 37, 49066)),
        ),
        migrations.AlterField(
            model_name='sekcja_pliku',
            name='data_utworzenia',
            field=models.DateField(default=datetime.datetime(2023, 5, 3, 11, 52, 37, 66299, tzinfo=datetime.timezone.utc)),
        ),
    ]
