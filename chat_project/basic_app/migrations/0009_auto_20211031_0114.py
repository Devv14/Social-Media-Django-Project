# Generated by Django 3.2.5 on 2021-10-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20211031_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mypost',
            name='post_count',
        ),
        migrations.AddField(
            model_name='mygroup',
            name='post_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
