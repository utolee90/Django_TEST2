# Generated by Django 3.1 on 2020-09-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.CharField(default='AnonymousUser', max_length=30),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.CharField(default='AnonymousUser', max_length=30),
        ),
    ]
