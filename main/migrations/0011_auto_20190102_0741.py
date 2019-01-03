# Generated by Django 2.1.2 on 2019-01-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20181231_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subsection',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='section',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]