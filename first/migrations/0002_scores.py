# Generated by Django 3.1 on 2020-09-04 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('math', models.IntegerField(max_length=3)),
                ('english', models.IntegerField(max_length=3)),
                ('science', models.IntegerField(max_length=3)),
            ],
        ),
    ]