# Generated by Django 2.2.5 on 2020-04-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200407_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.TextField(default=352, max_length=2),
            preserve_default=False,
        ),
    ]
