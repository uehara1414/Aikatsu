# Generated by Django 2.0 on 2017-12-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('word', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
    ]
