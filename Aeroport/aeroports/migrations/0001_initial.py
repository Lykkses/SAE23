# Generated by Django 4.0.5 on 2022-06-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeroports',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Avions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('compagnies', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compagnies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('pays_de_rattachement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pistes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('aeroport', models.CharField(max_length=100)),
                ('longueur', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Typeavions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('marque', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('longueurpistenecessaire', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vols',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pilote', models.CharField(max_length=100)),
                ('date_de_depart', models.DateField(blank=True, null=True)),
                ('date_de_darriver', models.DateField(blank=True, null=True)),
                ('heure_de_depart', models.TimeField()),
                ('heure_de_darriver', models.TimeField()),
                ('aeroport_de_darriver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Aeroport_Arrivee', to='aeroports.aeroports')),
                ('aeroport_de_depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Aeroport_Depart', to='aeroports.aeroports')),
                ('avions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aeroports.avions')),
            ],
        ),
    ]
