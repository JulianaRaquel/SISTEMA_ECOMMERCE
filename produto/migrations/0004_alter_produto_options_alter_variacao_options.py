# Generated by Django 4.0.6 on 2022-07-28 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_variacao_delete_varicacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
