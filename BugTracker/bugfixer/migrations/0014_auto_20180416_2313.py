# Generated by Django 2.0.3 on 2018-04-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0013_auto_20180409_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]