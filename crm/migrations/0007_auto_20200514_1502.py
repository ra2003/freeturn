# Generated by Django 2.2.12 on 2020-05-14 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20200506_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='channel',
        ),
        migrations.DeleteModel(
            name='Channel',
        ),
    ]
