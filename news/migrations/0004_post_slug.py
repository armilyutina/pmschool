# Generated by Django 2.2.5 on 2020-03-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.TextField(default=2110, max_length=150),
            preserve_default=False,
        ),
    ]
