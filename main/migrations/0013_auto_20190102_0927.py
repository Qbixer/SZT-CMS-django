# Generated by Django 2.1.2 on 2019-01-02 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190102_0829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsection',
            old_name='browser_title',
            new_name='tab_title',
        ),
        migrations.RemoveField(
            model_name='section',
            name='browser_title',
        ),
        migrations.AddField(
            model_name='section',
            name='tab_title',
            field=models.CharField(help_text='Optional. Maximum 50 characters.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.CharField(help_text='Optional. Maximum 10000 characters', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='contentType',
            field=models.ForeignKey(help_text='Optional. How the page should be displayed', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ContentType'),
        ),
        migrations.AlterField(
            model_name='section',
            name='deleted',
            field=models.BooleanField(default=False, help_text='Should page be marked as deleted. Possible to undo in admin panel'),
        ),
        migrations.AlterField(
            model_name='section',
            name='hidden',
            field=models.BooleanField(default=False, help_text='Required. Maximum 50 characters.'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order_number',
            field=models.IntegerField(default=0, help_text='Smaller number => More to the left. Sections sort ascending'),
        ),
        migrations.AlterField(
            model_name='section',
            name='should_display',
            field=models.BooleanField(default=True, help_text='Optional. Should page be displayed'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(help_text='Required. Maximum 50 characters.', max_length=50),
        ),
        migrations.AlterField(
            model_name='section',
            name='url',
            field=models.CharField(default='test', help_text='Required. Maximum 250 characters.', max_length=255),
            preserve_default=False,
        ),
    ]