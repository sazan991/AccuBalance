# Generated by Django 4.2.7 on 2024-01-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('items_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('amt_received', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('grand_total', models.IntegerField()),
                ('receivable_amt', models.IntegerField()),
            ],
        ),
    ]
