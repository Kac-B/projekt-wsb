# Generated by Django 2.2 on 2019-05-27 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seen',
            name='movieid',
        ),
        migrations.DeleteModel(
            name='Expect',
        ),
        migrations.DeleteModel(
            name='Seen',
        ),
    ]
