# Generated by Django 4.1.5 on 2023-06-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='off_price',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]
