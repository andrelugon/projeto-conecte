# Generated by Django 3.0.6 on 2020-10-23 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lg_distribuidora', '0002_auto_20201023_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dado',
            name='user',
        ),
    ]
