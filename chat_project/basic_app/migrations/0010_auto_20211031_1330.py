# Generated by Django 3.2.5 on 2021-10-31 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20211031_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mypost',
            options={'ordering': ('-published_date',)},
        ),
        migrations.AlterField(
            model_name='mypost',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
