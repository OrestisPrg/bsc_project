# Generated by Django 2.1.7 on 2019-04-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_progress_ch2ex1'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='ch2ex2',
            field=models.BooleanField(default=False),
        ),
    ]
