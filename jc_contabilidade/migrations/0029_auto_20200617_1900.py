# Generated by Django 3.0.6 on 2020-06-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jc_contabilidade', '0028_dado_link_de_acesso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dado',
            name='link_de_acesso',
        ),
        migrations.RemoveField(
            model_name='dado',
            name='logomarca',
        ),
    ]