# Generated by Django 2.2.7 on 2019-11-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pull_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pull_request_number', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('open_date', models.DateTimeField()),
                ('close_date', models.DateTimeField()),
            ],
        ),
    ]
