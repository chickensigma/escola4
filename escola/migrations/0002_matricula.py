# Generated by Django 5.0.8 on 2024-08-15 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.curso')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.estudante')),
            ],
        ),
    ]
