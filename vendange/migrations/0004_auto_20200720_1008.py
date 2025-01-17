# Generated by Django 3.0.3 on 2020-07-20 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20200719_2348'),
        ('entrants', '0003_materiels_orga'),
        ('vendange', '0003_auto_20200720_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marc',
            name='idMateriel',
        ),
        migrations.RemoveField(
            model_name='marc',
            name='idMillesime',
        ),
        migrations.AddField(
            model_name='marc',
            name='millesime',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administration.Millesime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marc',
            name='orga',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administration.Organisation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marc',
            name='pressoire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entrants.Materiels'),
            preserve_default=False,
        ),
    ]
