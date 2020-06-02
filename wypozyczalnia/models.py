import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Samochod(models.Model):
    marka = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    przebieg = models.IntegerField(default=0)
    nr_rej = models.CharField(max_length=7)
    miejsca = models.CharField(max_length=30)
    pakownosc = models.CharField(max_length=30)
    drzwi = models.CharField(max_length=30)
    skrzynia = models.CharField(max_length=30)
    klimatyzacja = models.CharField(max_length=30)
    paliwo = models.CharField(max_length=30)
    cena = models.IntegerField()
    kaucja = models.IntegerField()
    zdjecie = models.IntegerField()


class Miejsce(models.Model):
    miasto = models.CharField(max_length=50)
    ulica = models.CharField(max_length=50)
    numer = models.CharField(max_length=10)
    kod = models.CharField(max_length=6)
    telefon = models.IntegerField()
    adres = models.CharField(max_length=120)


class Rezerwacje(models.Model):
    klient = models.ForeignKey(User, on_delete=models.CASCADE)
    samochod = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    miejsce_odbioru = models.ForeignKey(Miejsce, related_name='odbior', on_delete=models.CASCADE)
    miejsce_zwrotu = models.ForeignKey(Miejsce, related_name='zwrot', on_delete=models.CASCADE)
    data_odbioru = models.DateField(default=datetime.date.today())
    data_zwrotu = models.DateField(default=datetime.date.today())