# Generated by Django 3.1.3 on 2021-03-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20210318_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='n_hit',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]