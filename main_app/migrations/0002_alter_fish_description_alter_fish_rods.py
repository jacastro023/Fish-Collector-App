# Generated by Django 4.0.4 on 2022-04-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='fish',
            name='rods',
            field=models.ManyToManyField(blank=True, to='main_app.rod'),
        ),
    ]
