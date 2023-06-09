# Generated by Django 4.1.7 on 2023-05-02 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0008_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plik',
            name='rodzic',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 21, 30, 38, 139820)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 21, 30, 38, 139794)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 21, 30, 38, 139811)),
        ),
        migrations.AlterField(
            model_name='sekcja_pliku',
            name='data_utworzenia',
            field=models.DateField(default=datetime.datetime(2023, 5, 2, 21, 30, 38, 154970)),
        ),
    ]
