# Generated by Django 3.0.3 on 2020-07-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrants', '0005_auto_20200725_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalparcelle',
            name='datebio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='parcelle',
            name='datebio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='parcelleetendue',
            name='proprietaire',
            field=models.CharField(max_length=50),
        ),
    ]
