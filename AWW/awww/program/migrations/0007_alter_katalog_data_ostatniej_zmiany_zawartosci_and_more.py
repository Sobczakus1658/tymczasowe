# Generated by Django 4.1.7 on 2023-05-02 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 19, 59, 2, 469902)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 19, 59, 2, 469877)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 19, 59, 2, 469894)),
        ),
        migrations.AlterField(
            model_name='sekcja_pliku',
            name='data_utworzenia',
            field=models.DateField(default=datetime.datetime(2023, 5, 2, 19, 59, 2, 486592)),
        ),
    ]