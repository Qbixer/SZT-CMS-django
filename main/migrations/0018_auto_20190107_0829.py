# Generated by Django 2.1.2 on 2019-01-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190102_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.RemoveField(
            model_name='section',
            name='contentType',
        ),
        migrations.RemoveField(
            model_name='subsection',
            name='content',
        ),
        migrations.RemoveField(
            model_name='subsection',
            name='contentType',
        ),
        migrations.AddField(
            model_name='section',
            name='restricted',
            field=models.BooleanField(default=False, help_text='Should page restricted for logged people.'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='restricted',
            field=models.BooleanField(default=False, help_text='Should page restricted for logged people.'),
        ),
    ]
