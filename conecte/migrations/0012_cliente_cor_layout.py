# Generated by Django 3.0.6 on 2020-10-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conecte', '0011_auto_20200702_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cor_layout',
            field=models.CharField(blank=True, choices=[('amarelo', 'amarelo'), ('azul', 'azul'), ('laranja', 'laranja'), ('cor-de-rosa', 'cor-de-rosa'), ('verde', 'verde'), ('vermelho', 'vermelho')], max_length=50, null=True),
        ),
    ]