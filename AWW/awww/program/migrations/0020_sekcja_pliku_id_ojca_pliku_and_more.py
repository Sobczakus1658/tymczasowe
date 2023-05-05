# Generated by Django 4.1.7 on 2023-05-03 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0019_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sekcja_pliku',
            name='id_ojca_pliku',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 16, 0, 20, 683291)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 16, 0, 20, 683269)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 16, 0, 20, 683286)),
        ),
        migrations.AlterField(
            model_name='sekcja_pliku',
            name='data_utworzenia',
            field=models.DateField(default=datetime.datetime(2023, 5, 3, 14, 0, 20, 698953, tzinfo=datetime.timezone.utc)),
        ),
    ]