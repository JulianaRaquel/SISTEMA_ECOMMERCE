# Generated by Django 4.0.6 on 2022-08-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='preco_marketing_promocional',
            new_name='preco_promocional',
        ),
    ]
