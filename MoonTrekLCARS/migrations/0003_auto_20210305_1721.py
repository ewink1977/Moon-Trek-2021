# Generated by Django 3.1.7 on 2021-03-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoonTrekLCARS', '0002_auto_20210305_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='rank',
            field=models.IntegerField(default=100),
        ),
    ]
