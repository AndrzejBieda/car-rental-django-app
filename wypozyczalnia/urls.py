from django.urls import path
from . import views

app_name = 'wypozyczalnia'

urlpatterns = [
    path('', views.index, name="index"),
    path("samochody/", views.samochody, name="samochody"),
    path("szczegoly/", views.szczegoly, name="szczegoly"),
    path("rezerwacja/", views.rezerwacja, name="rezerwacja"),
    path("rejestracja/", views.register, name="rejestracja"),
    path("logout/", views.logout_request, name="logout"),
    path("logowanie/", views.login_request, name="logowanie"),
]
