# Generated by Django 2.1 on 2018-08-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0005_auto_20180816_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='highDay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='lowDay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='priceChangeDay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coins',
            name='volumeDay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]