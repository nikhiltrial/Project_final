# Generated by Django 2.0.3 on 2018-03-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0006_auto_20180324_0305'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='staff',
            name='password',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='username',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
