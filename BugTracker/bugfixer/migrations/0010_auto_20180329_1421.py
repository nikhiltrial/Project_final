# Generated by Django 2.0.3 on 2018-03-29 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0009_staff_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
