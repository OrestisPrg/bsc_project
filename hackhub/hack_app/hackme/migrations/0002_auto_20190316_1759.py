# Generated by Django 2.1.7 on 2019-03-16 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
