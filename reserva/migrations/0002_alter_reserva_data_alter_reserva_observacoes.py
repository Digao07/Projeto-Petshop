# Generated by Django 4.2.4 on 2023-10-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
    ]
