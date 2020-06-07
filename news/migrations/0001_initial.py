# Generated by Django 2.2.5 on 2020-02-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='templates/image')),
            ],
        ),
    ]
