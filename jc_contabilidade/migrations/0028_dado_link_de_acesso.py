# Generated by Django 3.0.6 on 2020-06-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc_contabilidade', '0027_auto_20200610_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='dado',
            name='link_de_acesso',
            field=models.CharField(default=0, max_length=80),
            preserve_default=False,
        ),
    ]