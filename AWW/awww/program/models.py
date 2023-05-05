from django.db import models
import datetime
from django.utils import timezone

class Katalog(models.Model):
    # id_uzytkownika = models.IntegerField()
    rodzic = models.IntegerField(default = 0)
    nazwa = models.CharField(max_length=20)
    opcjonalny_opis = models.TextField(blank=True, default='')
    data_utworzenia = models.DateTimeField(default= datetime.datetime.now())
    # wlasciciel = models.IntegerField()
    znacznik_dostepnosci = models.BooleanField(default=True)
    data_zmiany_znacznika = models.DateTimeField(default=datetime.datetime.now())
    data_ostatniej_zmiany_zawartosci = models.DateTimeField(default=datetime.datetime.now() )

    @classmethod
    def create(cls, katalog_nazwa, rodzic):
        katalog = Katalog(
            # id_uzytkownika = 1,
            rodzic = rodzic,
            nazwa = katalog_nazwa,
        )
        return katalog
    
    def __str__(self):
        podkatalogi = Katalog.objects.raw("""Select * from program_katalog  where rodzic = %s and znacznik_dostepnosci = 1 """, [self.id])
        podpliki = Plik.objects.raw("""Select * from program_plik  where rodzic = %s and znacznik_dostepnosci = 1 """, [self.id])
        wynik = '<li>' + self.nazwa.replace('<', '&lt;').replace('>','&gt;')
        if podkatalogi or podpliki:
            wynik += '<ul>'
            for element in podkatalogi:
                wynik += element.__str__()
            for element in podpliki:
                wynik += element.__str__()
            wynik += '</ul>'
        wynik += '</li>'
        return wynik
# ustawić że jedno jest opcjonalne

class Plik(models.Model):
    nazwa = models.CharField(max_length=10)
    tresc = models.TextField(default ='')
    rodzic = models.IntegerField(default = 0)
    opcjonalny_opis = models.TextField()
    data_utworzenia = models.DateField()
    # wlasciciel = models.IntegerField()
    znacznik_dostepnosci = models.BooleanField()
    data_zmiany_znacznika = models.DateField()
    data_ostatniej_zmiany_zawartosci = models.DateField()

    @classmethod
    def create(cls, plik_nazwa, rodzic, tresc):
        plik = Plik(
            nazwa = plik_nazwa,
            tresc = tresc,
            rodzic = rodzic,
            # opcjonalny_opis = plik_opis,
            data_utworzenia = datetime.datetime.now(),
        # wlasciciel = plik_wlasciciel,
        znacznik_dostepnosci = 1,
        data_zmiany_znacznika = datetime.datetime.now(),
        data_ostatniej_zmiany_zawartosci= datetime.datetime.now() 
        )
        return plik
    
    def __str__(self):
        return '<li>' + '<a href="wyswietl_kod/'+str(self.id)+'"> ' + self.nazwa+ '</a>' + '</li>'


class Uzytkownik(models.Model):
    nazwa = models.CharField(max_length=10)
    login = models.CharField(max_length=10)
    haslo = models.CharField(max_length=10)

class Rodzaj_sekcji(models.Model):
    nazwa = models.CharField(max_length= 50)
    @classmethod
    def create(cls, nazwa):
        nazwa = nazwa

class Status_sekcji(models.Model):
    name = models.CharField(max_length= 50)
    @classmethod
    def create(clas, name):
        name = name

class Dane_statusu(models.Model):
    name = models.CharField(max_length= 50)
    @classmethod
    def create(clas, name):
        name = name


class Sekcja_pliku(models.Model):
    # id_ojca_sekcji = models.IntegerField()
    id_ojca_pliku = models.IntegerField(default=0)
    opcjonalna_nazwa = models.CharField(max_length=20, default='')
    opcjonalny_opis = models.TextField (default='')
    data_utworzenia = models.DateField(default=timezone.now())
    znacznik_dostepnosci = models.BooleanField(default=True)

    poczatek_sekcji = models.IntegerField(default=0)
    koniec_sekcji = models.IntegerField(default=0)

    rodzaj_sekcji = models.IntegerField()
    status_sekcji = models.IntegerField(default = 0)
    dane_statusu = models.IntegerField(default = 0)
    tresc = models.TextField()
    @classmethod
    def create(cls, nazwa_sekcji, opis_sekcji, tresc_sekcji, poczatek_sekcji, koniec_sekcji, id_rodzaju_sekcji, rodzic):
        sekcja_pliku = Sekcja_pliku(
            opcjonalna_nazwa = nazwa_sekcji,
            id_ojca_pliku = rodzic,
            # id_ojca_sekcji = id_ojca_sekcji,
            opcjonalny_opis = opis_sekcji,
            data_utworzenia = timezone.now(),
            rodzaj_sekcji = id_rodzaju_sekcji ,
            znacznik_dostepnosci = 1,
            poczatek_sekcji = poczatek_sekcji,
            koniec_sekcji = koniec_sekcji,
            tresc = tresc_sekcji,
        )
        return sekcja_pliku

