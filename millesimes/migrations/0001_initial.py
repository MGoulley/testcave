# Generated by Django 3.0.3 on 2020-02-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Millesime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField()),
                ('nomMillesime', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'millesime',
            },
        ),
    ]