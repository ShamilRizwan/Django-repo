# Generated by Django 4.1.1 on 2022-10-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='number',
            field=models.IntegerField(verbose_name=20),
        ),
    ]
