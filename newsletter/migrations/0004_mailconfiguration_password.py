# Generated by Django 2.1.2 on 2019-01-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20190126_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailconfiguration',
            name='password',
            field=models.CharField(default='asd', max_length=255),
            preserve_default=False,
        ),
    ]
