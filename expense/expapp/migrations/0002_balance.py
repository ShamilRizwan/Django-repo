# Generated by Django 4.1.1 on 2022-10-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balamt', models.IntegerField(verbose_name=20)),
            ],
        ),
    ]
