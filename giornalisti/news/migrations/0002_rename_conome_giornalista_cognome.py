# Generated by Django 3.2.9 on 2021-11-06 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giornalista',
            old_name='conome',
            new_name='cognome',
        ),
    ]