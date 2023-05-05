from django.urls import path

from . import views
app_name = 'program'
urlpatterns = [
    path('', views.index, name='index'),
    path('usun_katalog', views.usun_katalog, name='usun_katalog'),
    path('usun_plik', views.usun_plik, name='usun_plik'),
    path('stworz_katalog', views.stworz_katalog, name='stworz_katalog'),
    path('stworz_plik', views.stworz_plik, name='stworz_plik'),
    path('zlacz_sekcje', views.zlacz_sekcje, name='zlacz_sekcje'),
    path('dodaj_sekcje', views.dodaj_sekcje, name='dodaj_sekcje'),
    path('tworzenie_katalogu', views.tworzenie_katalogu, name = 'tworzenie_katalogu'),
    path('usuwanie_katalogu', views.usuwanie_katalogu, name = 'usuwanie_katalogu'),
    path('usuwanie_pliku', views.usuwanie_pliku, name ='usuwanie_pliku'),
    path('tworzenie_pliku', views.tworzenie_pliku, name ='tworzenie_pliku'),
    path('wyswietl_kod/<int:id_pliku>', views.wyswietl_kod, name='wyswietl_kod'),
    path('usuwanie_sekcji', views.usuwanie_sekcji, name ='usuwanie_sekcji'),
    path('laczenie_sekcji', views.laczenie_sekcji, name ='laczenie_sekcji'),
    path('zlacz_sekcje', views.zlacz_sekcje, name ='zlacz_sekcje'),
    path('usun_sekcje', views.usun_sekcje, name ='usun_sekcje'),
    # path('tworzenie_sekcji', views.tworzenie_sekcji, name = 'tworzenie_sekcji')
]