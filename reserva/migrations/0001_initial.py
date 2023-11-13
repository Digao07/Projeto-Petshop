# Generated by Django 4.2.4 on 2023-10-20 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Petshop')),
                ('rua', models.CharField(max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('data', models.DateField(help_text='dd/mm/aaaa', verbose_name='Data')),
                ('turno', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde')], max_length=10, verbose_name='Turno')),
                ('tamanho', models.CharField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')], max_length=10, verbose_name='Tamanho do PET')),
                ('observacoes', models.TextField(blank=True)),
                ('petshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.petshop')),
            ],
            options={
                'verbose_name': 'Reserva de Banho',
                'verbose_name_plural': 'Reservas de Banho',
            },
        ),
    ]
