# Generated by Django 3.0.3 on 2020-07-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendange', '0002_auto_20200720_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benne',
            old_name='idMateriel',
            new_name='benne',
        ),
        migrations.RenameField(
            model_name='benne',
            old_name='idOperateur',
            new_name='operateur',
        ),
    ]
