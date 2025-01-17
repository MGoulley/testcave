# Generated by Django 3.0.3 on 2020-08-01 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendange', '0004_auto_20200720_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marc',
            name='volumeMarc',
            field=models.FloatField(blank=True),
        ),
        migrations.CreateModel(
            name='BennesMarc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volBenne', models.FloatField()),
                ('benne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendange.Benne')),
                ('marc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendange.Marc')),
            ],
            options={
                'db_table': 'bennes-marc',
            },
        ),
        migrations.RemoveField(
            model_name='marc',
            name='bennes',
        ),
        migrations.AddField(
            model_name='marc',
            name='bennes',
            field=models.ManyToManyField(through='vendange.BennesMarc', to='vendange.Benne'),
        ),
    ]
