# Generated by Django 2.1 on 2018-08-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0006_auto_20180816_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='priceChangeRateDay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
