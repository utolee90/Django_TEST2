# Generated by Django 3.1 on 2020-09-11 09:40

from django.db import migrations, models
import first.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20200911_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to=first.models.upload_to),
        ),
        migrations.AlterField(
            model_name='students',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]