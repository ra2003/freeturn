# Generated by Django 2.0.9 on 2019-01-15 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20190115_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='technologies',
        ),
    ]