# Generated by Django 2.0.3 on 2018-03-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tickets_url', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('ON', 'OPEN'), ('IS', 'IN PROGRESS'), ('RW', 'REVIEW'), ('CD', 'CLOSED')], max_length=1)),
                ('num_of_ppl_affected', models.IntegerField(null=True)),
                ('url', models.TextField()),
            ],
        ),
    ]