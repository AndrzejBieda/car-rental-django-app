import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from wypozyczalnia.forms import PlaceAndDate, Sam, Sam1
from wypozyczalnia.models import Samochod, Miejsce, Rezerwacje


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PlaceAndDate(request.POST)
        if form.is_valid():
            request.session['miejsce_odb'] = form.cleaned_data.get('miejsce_odb')
            request.session['miejsce_zwr'] = form.cleaned_data.get('miejsce_zwr')
            request.session['data_odb'] = form.cleaned_data.get('data_odb')
            request.session['data_zwr'] = form.cleaned_data.get('data_zwr')
            return HttpResponseRedirect('samochody/')
    else:
        x = datetime.date.today()
        today = x.strftime("%Y-%m-%d")
        form = PlaceAndDate()
        return render(request, 'wypozyczalnia/index.html',
                      {"samochody": Samochod.objects.all, "miejsca": Miejsce.objects.all, "today": today, "form": form})


def samochody(request):
    if request.method == 'POST':
        form = Sam(request.POST)
        if form.is_valid():
            request.session['sam'] = form.cleaned_data.get('sam')
            return HttpResponseRedirect('../szczegoly/')
    else:
        dataodb = datetime.datetime.strptime(request.session['data_odb'], "%Y-%m-%d").date()
        datazwr = datetime.datetime.strptime(request.session['data_zwr'], "%Y-%m-%d").date()
        dni = ((datazwr - dataodb).days) + 1
        form = Sam()
        # b = Rezerwacje(klient=request.user, samochod_id=1,
        #                miejsce_odbioru=Miejsce.objects.get(adres=request.session['miejsce_odb']),
        #                miejsce_zwrotu=Miejsce.objects.get(adres=request.session['miejsce_zwr']),
        #                data_odbioru=dataodb, data_zwrotu=datazwr)
        # b.save()
        return render(request, 'wypozyczalnia/samochody.html',
                      {"samochody": Samochod.objects.all(),
                       "miejsce_odb": request.session['miejsce_odb'],
                       "miejsce_zwr": request.session['miejsce_zwr'],
                       "data_odb": request.session['data_odb'],
                       "data_zwr": request.session['data_zwr'],
                       "dni": dni,
                       "form": form
                       })


def szczegoly(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Sam1(request.POST)
            if form.is_valid():
                request.session['sam1'] = form.cleaned_data.get('sam')
                return HttpResponseRedirect('../rezerwacja/')
        else:
            dataodb = datetime.datetime.strptime(request.session['data_odb'], "%Y-%m-%d").date()
            datazwr = datetime.datetime.strptime(request.session['data_zwr'], "%Y-%m-%d").date()
            dni = ((datazwr - dataodb).days) + 1
            form = Sam()
            # b = Rezerwacje(klient=request.user, samochod_id=1,
            #                miejsce_odbioru=Miejsce.objects.get(adres=request.session['miejsce_odb']),
            #                miejsce_zwrotu=Miejsce.objects.get(adres=request.session['miejsce_zwr']),
            #                data_odbioru=dataodb, data_zwrotu=datazwr)
            # b.save()
            return render(request, 'wypozyczalnia/szczegoly.html',
                          {"s": Samochod.objects.get(id=request.session['sam']),
                           "miejsce_odb": request.session['miejsce_odb'],
                           "miejsce_zwr": request.session['miejsce_zwr'],
                           "data_odb": request.session['data_odb'],
                           "data_zwr": request.session['data_zwr'],
                           "dni": dni,
                           "form": form,
                           })
    else:
        return redirect('wypozyczalnia:logowanie')


def rezerwacja(request):
    if request.user.is_authenticated:
        dataodb = datetime.datetime.strptime(request.session['data_odb'], "%Y-%m-%d").date()
        datazwr = datetime.datetime.strptime(request.session['data_zwr'], "%Y-%m-%d").date()
        b = Rezerwacje(klient=request.user, samochod_id=request.session['sam1'],
                       miejsce_odbioru=Miejsce.objects.get(adres=request.session['miejsce_odb']),
                       miejsce_zwrotu=Miejsce.objects.get(adres=request.session['miejsce_zwr']),
                       data_odbioru=dataodb, data_zwrotu=datazwr)
        b.save()
        return render(request, 'wypozyczalnia/rezerwacja.html',
                      {"s": Samochod.objects.get(id=request.session['sam1']),
                       "miejsce_odb": request.session['miejsce_odb'],
                       "miejsce_zwr": request.session['miejsce_zwr'],
                       "data_odb": request.session['data_odb'],
                       "data_zwr": request.session['data_zwr'],
                       })
    else:
        return redirect('wypozyczalnia:logowanie')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="wypozyczalnia/rejestracja.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request=request,
                  template_name="wypozyczalnia/rejestracja.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Wylogowano!")
    return redirect("/")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Jesteś zalogowany jako {username}")
                return redirect('/')
            else:
                messages.error(request, "Zły login lub hasło.")
        else:
            messages.error(request, "Zły login lub hasło.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="wypozyczalnia/logowanie.html",
                  context={"form": form})
