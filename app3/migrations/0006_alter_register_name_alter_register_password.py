# Generated by Django 4.1.5 on 2023-06-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0005_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
