# Generated by Django 4.1 on 2022-08-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_order_delivery_charge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Active'), (1, 'Delivered'), (2, 'Cancelled')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.SmallIntegerField(choices=[(0, 'Paid'), (1, 'Unpaid'), (2, 'Due')], default=1),
        ),
    ]
