# Generated by Django 3.0.2 on 2020-01-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samochody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('przebieg', models.IntegerField(default=0)),
                ('nr_rej', models.CharField(max_length=7)),
                ('miejsca', models.CharField(max_length=30)),
                ('pakownosc', models.CharField(max_length=30)),
                ('drzwi', models.CharField(max_length=30)),
                ('skrzynia', models.CharField(max_length=30)),
                ('klimatyzacja', models.CharField(max_length=30)),
                ('paliwo', models.CharField(max_length=30)),
                ('cena', models.IntegerField()),
                ('kaucja', models.IntegerField()),
                ('zdjecie', models.IntegerField()),
            ],
        ),
    ]
