# Generated by Django 2.2 on 2020-01-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Phone Name', max_length=200)),
                ('brand', models.CharField(default='Brand Name', max_length=200)),
                ('Camera', models.CharField(default='Camera Details', max_length=200)),
                ('Processor', models.CharField(default='Processor Name', max_length=200)),
                ('price', models.FloatField(default=0.0, max_length=200)),
            ],
        ),
    ]
