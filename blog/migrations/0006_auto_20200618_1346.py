# Generated by Django 2.2.12 on 2020-06-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='awards',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='involvement',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]