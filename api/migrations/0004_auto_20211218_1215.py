# Generated by Django 2.2.11 on 2021-12-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211119_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='contract_type',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='job_category',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='location',
            field=models.CharField(default='', max_length=300),
        ),
    ]
