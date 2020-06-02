from django.contrib import admin
from wypozyczalnia.models import Samochod, Miejsce, Rezerwacje

# Register your models here.


admin.site.register(Samochod)
admin.site.register(Miejsce)
admin.site.register(Rezerwacje)