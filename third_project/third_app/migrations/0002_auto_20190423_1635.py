# Generated by Django 2.2 on 2019-04-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='profile_pics',
            new_name='pics',
        ),
    ]