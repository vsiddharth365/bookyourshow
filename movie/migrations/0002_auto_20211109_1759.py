# Generated by Django 3.2.9 on 2021-11-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecast',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cast'),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='movie_poster'),
        ),
    ]
