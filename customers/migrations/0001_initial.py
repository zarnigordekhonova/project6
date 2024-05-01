# Generated by Django 5.0.4 on 2024-05-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='customer_info1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
