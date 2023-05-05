# Generated by Django 4.1.7 on 2023-05-03 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0013_alter_katalog_data_ostatniej_zmiany_zawartosci_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dane_statusu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj_sekcji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status_sekcji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_ostatniej_zmiany_zawartosci',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 26, 55, 757086)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 26, 55, 757062)),
        ),
        migrations.AlterField(
            model_name='katalog',
            name='data_zmiany_znacznika',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 13, 26, 55, 757079)),
        ),
    ]
