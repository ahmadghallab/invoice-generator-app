# Generated by Django 2.0.1 on 2018-11-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_auto_20181107_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='discount',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='qty',
            field=models.FloatField(blank=True, default=1),
        ),
    ]
