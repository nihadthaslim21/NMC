# Generated by Django 4.2.1 on 2023-07-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0011_cartitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ManyToManyField(to='app3.products')),
            ],
        ),
    ]
