# Generated by Django 3.1.4 on 2020-12-16 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=30, verbose_name='Último Nome')),
                ('email', models.EmailField(max_length=60, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Senha')),
                ('birthday', models.DateField(verbose_name='Data de nascimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer', verbose_name='Cliente')),
            ],
        ),
    ]
