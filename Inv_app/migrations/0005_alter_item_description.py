# Generated by Django 5.0.4 on 2024-04-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inv_app', '0004_alter_item_name_alter_item_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=20),
        ),
    ]
