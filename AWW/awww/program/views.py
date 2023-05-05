from django.shortcuts import render
from program.models import Katalog, Plik, Sekcja_pliku, Rodzaj_sekcji
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import re
def index(request):
    opcje = Katalog.objects.raw(
        """Select * from program_katalog where rodzic = 0 and znacznik_dostepnosci = 1"""
    )
    podpliki = Plik.objects.raw("""Select * from program_plik  where rodzic = 0 and znacznik_dostepnosci = 1 """)

    katalogi = Katalog.objects.all()
    pliki = Plik.objects.all()
    sekcje = Sekcja_pliku.objects.all()
    context = {
        'katalogi': katalogi,
        'podpliki': podpliki,
        'pliki' : pliki,
        'opcje' : opcje,
        'sekcje': sekcje
    }
    return render(request, 'program/index.html', context)

def dodaj_sekcje(request):
    nazwa_sekcji = request.POST['nazwa_sekcji']
    opis_sekcji = request.POST['opis_sekcji']
    id_pliku = int(request.POST['id_pliku'])
    id_ojca_sekcji = int (request.POST['id_ojca_sekcji'])
    tresc = request.POST['tresc']
    poczatek_sekcji = 0
    koniec_sekcji = 17
    nowa_sekcja = Sekcja_pliku.create(id_pliku, id_ojca_sekcji, nazwa_sekcji, opis_sekcji,
                                      tresc, poczatek_sekcji, koniec_sekcji)
    nowa_sekcja.save()
    return HttpResponseRedirect(reverse('program:index'))

def zlacz_sekcje(request):
    id_pierwszej_sekcji = int(request.POST["id_pierwszej_sekcji"])
    id_drugiej_sekcji = int (request.POST["id_drugiej_sekcji"])
    pierwsza_sekcja = get_object_or_404(Sekcja_pliku, pk = id_pierwszej_sekcji)
    druga_sekcja = get_object_or_404(Sekcja_pliku, pk = id_drugiej_sekcji)
    id_ojca_sekcji = pierwsza_sekcja.id_ojca_sekcji
    id_ojca_pliku = pierwsza_sekcja.id_ojca_pliku
    opcjonalna_nazwa = pierwsza_sekcja.opcjonalna_nazwa
    opcjonalna_opis = pierwsza_sekcja.opcjonalny_opis
    tresc = pierwsza_sekcja.tresc + druga_sekcja.tresc
    poczatek_sekcji = min(pierwsza_sekcja.poczatek_sekcji, druga_sekcja.poczatek_sekcji)
    koniec_sekcji = max(pierwsza_sekcja.koniec_sekcji, druga_sekcja.koniec_sekcji)
    nowa_sekcja = Sekcja_pliku.create(id_ojca_pliku, id_ojca_sekcji, opcjonalna_nazwa, opcjonalna_opis,
                                      tresc, poczatek_sekcji, koniec_sekcji)
    nowa_sekcja.save()
    # pierwsza_sekcja.znacznik_dostepnosci = 0
    # druga_sekcja.znacznik_dostepnosci = 0
    pierwsza_sekcja.delete()
    druga_sekcja.delete()
    return HttpResponseRedirect(reverse('program:index'))

def tworzenie_katalogu(request):
    katalogi = Katalog.objects.filter(znacznik_dostepnosci =1)
    context = {
        'katalogi': katalogi,
    }
    return render(request, 'program/tworzenie_katalogu.html', context)

def tworzenie_pliku(request):
    katalogi = Katalog.objects.filter(znacznik_dostepnosci =1)
    context = {
        'katalogi': katalogi,
    }
    return render(request, 'program/tworzenie_pliku.html', context)

def stworz_katalog(request):
    katalog_nazwa = request.POST["nazwa"]
    rodzic = int(request.POST["rodzic"])
    nowy_katalog = Katalog.create(katalog_nazwa, rodzic)
    nowy_katalog.save()  
    return HttpResponseRedirect(reverse('program:index'))

def rodzaj_linii(linia):
    match = re.fullmatch(".*__asm__.*", linia)
    if match != None :
        return "assembler"
    match = re.fullmatch("\s*\/\/.*", linia)
    if match != None :
        return "komentarz"
    match = re.fullmatch("\s*#.*", linia)
    if match != None :
        return "dyrektywa"
    match = re.fullmatch("\s*(int|double|float|char).*\;", linia)
    if match != None :
        return "deklaracja"
    return "procedura"

def podziel(tresc, rodzic):
    list = tresc.splitlines()
    tresc_w_sekcji = ""
    aktualny_licznik = 1
    rodzaj_sekcji = None
    poczatek_sekcji = 1
    for element in list :
        if element == '':
            aktualny_licznik = aktualny_licznik + 1
            tresc_w_sekcji = tresc_w_sekcji +'\n'
            continue
        rodzaj = rodzaj_linii(element)
        if rodzaj == rodzaj_sekcji :
            tresc_w_sekcji+= element + '\n'
        else :
            if aktualny_licznik > 1 :
                nowy_rodzaj = Rodzaj_sekcji.objects.get(nazwa = rodzaj_sekcji)
                nowa_sekcja = Sekcja_pliku.create('','',tresc_w_sekcji,poczatek_sekcji, aktualny_licznik - 1, nowy_rodzaj.id, rodzic)
                nowa_sekcja.save()
                rodzaj_sekcji = rodzaj
                tresc_w_sekcji = element
                poczatek_sekcji = aktualny_licznik
            else :
                rodzaj_sekcji = rodzaj
                tresc_w_sekcji = element
                poczatek_sekcji = aktualny_licznik
        aktualny_licznik = aktualny_licznik + 1
    nowy_rodzaj = Rodzaj_sekcji.objects.get(nazwa = rodzaj_sekcji)
    nowa_sekcja = Sekcja_pliku.create('','',tresc_w_sekcji,poczatek_sekcji, aktualny_licznik - 1, nowy_rodzaj.id, rodzic)
    nowa_sekcja.save()

def stworz_plik(request):
    plik = request.FILES['nazwa']
    rodzic = int(request.POST["rodzic"])
    tresc = plik.read().decode("utf-8")
    nowy_plik = Plik.create(plik.name, rodzic, tresc)
    nowy_plik.save() 
    podziel(tresc, nowy_plik.id) 
    return HttpResponseRedirect(reverse('program:index'))

def usuwanie_katalogu(request):
    katalogi = Katalog.objects.filter(znacznik_dostepnosci =1 )
    context = {
        'katalogi': katalogi,
    }
    return render(request, 'program/usuwanie_katalogu.html', context)

def usuwanie_pliku(request):
    pliki = Plik.objects.filter(znacznik_dostepnosci =1 )
    context = {
        'pliki': pliki,
    }
    return render(request, 'program/usuwanie_pliku.html', context)

def usun_rekurencyjnie(folder):
    pass
    katalogi = Katalog.objects.filter(rodzic = folder.id)
    for element in katalogi:
        usun_rekurencyjnie(element)
    pliki = Plik.objects.filter(rodzic = folder.id)
    for element in pliki:
        element.znacznik_dostepnosci = 0
        element.data_zmiany_znacznika = timezone.now()
        element.save()
    folder.znacznik_dostepnosci = 0
    folder.data_zmiany_znacznika = timezone.now()
    folder.save()

def usun_katalog(request):
    katalog = int(request.POST["katalog"])
    folder = get_object_or_404(Katalog, pk = katalog)
    usun_rekurencyjnie(folder)
    return HttpResponseRedirect(reverse('program:index'))

def usun_plik(request):
    plik = int(request.POST["plik"])
    katalogi = Katalog.objects.filter(znacznik_dostepnosci =1)
    context = {
        'katalogi': katalogi,
    }
    plik_do_usuniecia = get_object_or_404(Plik, pk = plik)
    plik_do_usuniecia.znacznik_dostepnosci = 0
    plik_do_usuniecia.save()
    return HttpResponseRedirect(reverse('program:index'), context)

def wyswietl_kod(request, id_pliku):
    list = Plik.objects.get(id = id_pliku).tresc
    context = {
        'list' : list
    }
    return render(request, 'program/debuger.html', context)

def usuwanie_sekcji(request):
    sekcje = Sekcja_pliku.objects.filter()
    context = {
        'pliki': sekcje,
    }
    return render(request, 'program/usuwanie_sekcji.html', context)

def laczenie_sekcji(request):
    pliki = Plik.objects.filter(znacznik_dostepnosci =1)
    context = {
        'pliki': pliki,
    }
    return render(request, 'program/laczenie_sekcji.html', context)

def usun_sekcje(request):
    pass

def zlacz_sekcje(request):
    pass
