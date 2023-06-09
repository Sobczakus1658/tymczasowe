# Generated by Django 4.1.7 on 2023-05-03 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0011_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plik',
            name='tresc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 12, 9, 20, 561672)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 12, 9, 20, 561644)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 12, 9, 20, 561663)),
        ),
        migrations.AlterField(
            model_name='sekcja_pliku',
            name='data_utworzenia',
            field=models.DateField(),
        ),
    ]
