# Generated by Django 4.2.1 on 2023-06-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=32)),
            ],
        ),
    ]