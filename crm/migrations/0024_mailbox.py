# Generated by Django 2.0.9 on 2018-11-19 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0007_auto_20181115_1822'),
        ('crm', '0023_auto_20181115_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailbox',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('django_mailbox.mailbox',),
        ),
    ]
