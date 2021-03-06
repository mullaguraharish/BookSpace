# Generated by Django 3.1.7 on 2021-04-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customer_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
