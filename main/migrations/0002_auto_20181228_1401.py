# Generated by Django 2.1.2 on 2018-12-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_html',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
