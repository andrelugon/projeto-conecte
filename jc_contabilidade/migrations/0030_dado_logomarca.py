# Generated by Django 3.0.6 on 2020-06-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc_contabilidade', '0029_auto_20200617_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='dado',
            name='logomarca',
            field=models.ImageField(blank=True, null=True, upload_to='logomarca'),
        ),
    ]
