# Generated by Django 3.1.4 on 2021-03-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrigeapp', '0003_auto_20210315_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_mark',
            name='manual_mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='manual_mark'),
        ),
        migrations.AlterField(
            model_name='activity_mark',
            name='mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark'),
        ),
        migrations.AlterField(
            model_name='competence_mark',
            name='mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark'),
        ),
        migrations.AlterField(
            model_name='exercise_mark',
            name='manual_mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='manual_mark'),
        ),
        migrations.AlterField(
            model_name='exercise_mark',
            name='mark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='mark'),
        ),
    ]
