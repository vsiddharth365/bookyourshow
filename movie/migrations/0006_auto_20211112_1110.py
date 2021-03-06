# Generated by Django 3.2.9 on 2021-11-12 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20211110_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('no_of_rows', models.IntegerField()),
                ('no_of_columns', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('rating', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ShowDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('price', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_movie', to='movie.moviedetail')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_screen', to='movie.screen')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_theatre', to='movie.theatre')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screen', to='movie.theatre'),
        ),
    ]
