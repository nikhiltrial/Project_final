# Generated by Django 2.0.3 on 2018-05-10 02:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0025_auto_20180510_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='num_of_ppl_affected',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
