# Generated by Django 3.2.7 on 2021-09-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManager', '0019_product_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty_in_stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmovements',
            name='qty_to_be_moved',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
