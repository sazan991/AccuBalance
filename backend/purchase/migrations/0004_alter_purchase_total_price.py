# Generated by Django 5.0.1 on 2024-03-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_alter_purchase_payable_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
