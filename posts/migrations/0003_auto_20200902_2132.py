# Generated by Django 3.1 on 2020-09-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_pavada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pavada',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
