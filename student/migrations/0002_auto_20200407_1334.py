# Generated by Django 2.2.5 on 2020-04-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='img',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='title',
        ),
        migrations.AlterField(
            model_name='ad',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
