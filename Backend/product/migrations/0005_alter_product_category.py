# Generated by Django 4.1 on 2022-08-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_status_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.SmallIntegerField(choices=[(0, 'Fruits'), (1, 'Vegetable'), (2, 'Fish'), (3, 'Dry Fruits'), (4, 'Egg'), (5, 'Chicken'), (6, 'Other')], default=1),
            preserve_default=False,
        ),
    ]
