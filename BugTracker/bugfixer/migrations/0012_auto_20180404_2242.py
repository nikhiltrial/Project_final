# Generated by Django 2.0.3 on 2018-04-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugfixer', '0011_auto_20180404_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('CLOSED', 'CLOSED')], max_length=30),
        ),
    ]
