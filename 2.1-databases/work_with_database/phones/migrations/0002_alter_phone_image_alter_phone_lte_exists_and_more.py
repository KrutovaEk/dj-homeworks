# Generated by Django 5.0.6 on 2024-05-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
