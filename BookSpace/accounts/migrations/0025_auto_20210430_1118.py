# Generated by Django 3.1.7 on 2021-04-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_product_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
    ]
