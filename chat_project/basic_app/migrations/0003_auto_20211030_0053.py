# Generated by Django 3.2.5 on 2021-10-29 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_mygroup_mypost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygroup',
            name='member_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mygroup',
            name='post_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='basic_app.mygroup'),
        ),
    ]
