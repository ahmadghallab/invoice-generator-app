# Generated by Django 2.1.3 on 2018-11-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0025_auto_20181114_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_no',
            field=models.IntegerField(null=True),
        ),
    ]