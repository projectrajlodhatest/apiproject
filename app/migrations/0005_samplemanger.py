# Generated by Django 3.2.7 on 2021-12-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211210_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleManger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
