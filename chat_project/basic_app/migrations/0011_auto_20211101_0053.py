# Generated by Django 3.2.5 on 2021-10-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0010_auto_20211031_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='mygroup',
            name='add_string',
            field=models.CharField(default='.', max_length=1024),
        ),
        migrations.AddField(
            model_name='mygroup',
            name='remove_string',
            field=models.CharField(default='.', max_length=1024),
        ),
    ]