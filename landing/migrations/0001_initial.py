# Generated by Django 2.2.5 on 2019-09-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('idade', models.CharField(max_length=50, verbose_name='idade')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
            ],
        ),
    ]