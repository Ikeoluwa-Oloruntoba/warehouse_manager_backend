# Generated by Django 3.2.7 on 2021-09-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManager', '0015_alter_location_location_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmovements',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
