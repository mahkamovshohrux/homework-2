# Generated by Django 4.2.5 on 2023-09-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('lastname2', models.CharField(max_length=30)),
                ('deta2', models.DateField()),
            ],
        ),
    ]