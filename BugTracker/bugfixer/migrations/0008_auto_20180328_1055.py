# Generated by Django 2.0.3 on 2018-03-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0007_auto_20180328_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
