# Generated by Django 3.2.9 on 2021-11-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='contenuto',
            field=models.TextField(),
        ),
    ]
