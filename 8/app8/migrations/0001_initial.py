# Generated by Django 4.2.5 on 2023-09-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name8', models.CharField(max_length=40)),
                ('lastname8', models.CharField(max_length=20)),
                ('data8', models.DateField()),
            ],
        ),
    ]