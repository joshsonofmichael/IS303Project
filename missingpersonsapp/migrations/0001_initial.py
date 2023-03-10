# Generated by Django 4.1.2 on 2022-12-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Missing_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_missing', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('firstName', models.CharField(max_length=40)),
                ('age_at_missing', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('gender', models.CharField(max_length=1)),
                ('race', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'Missing Persons',
            },
        ),
    ]
