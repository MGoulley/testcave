# Generated by Django 3.0.3 on 2020-02-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelles', '0002_auto_20200227_2300'),
        ('bennes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benne',
            name='parcelles',
            field=models.ManyToManyField(blank=True, to='parcelles.Parcelle'),
        ),
    ]