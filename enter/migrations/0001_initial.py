# Generated by Django 2.2.5 on 2020-03-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=200)),
                ('town', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('numberPhone', models.IntegerField()),
            ],
        ),
    ]
