# Generated by Django 3.1.7 on 2021-03-05 08:03

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MoonTrekStories', '0003_auto_20210304_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('faction', models.IntegerField(default=0)),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.ManyToManyField(related_name='ships', to='MoonTrekStories.MoonTrekStories')),
            ],
        ),
        migrations.CreateModel(
            name='PlacesAndItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.ManyToManyField(related_name='places', to='MoonTrekStories.MoonTrekStories')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rank', models.IntegerField(default=0)),
                ('content', tinymce.models.HTMLField()),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.ManyToManyField(related_name='characters', to='MoonTrekStories.MoonTrekStories')),
            ],
        ),
    ]
