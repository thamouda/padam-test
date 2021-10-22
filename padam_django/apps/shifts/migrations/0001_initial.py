# Generated by Django 3.2.5 on 2021-10-20 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0001_initial'),
        ('fleet', '0002_alter_driver_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Bus stop name')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geography.place')),
            ],
        ),
        migrations.CreateModel(
            name='BusTravelTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('stop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shifts.busstop')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='BusShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='fleet.bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.driver')),
                ('stop', models.ManyToManyField(to='shifts.BusTravelTime')),
            ],
        ),
    ]