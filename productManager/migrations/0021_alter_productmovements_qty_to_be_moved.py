# Generated by Django 3.2.7 on 2021-09-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManager', '0020_auto_20210929_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmovements',
            name='qty_to_be_moved',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
