# Generated by Django 2.1.3 on 2018-11-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0026_order_order_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='enter_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='exit_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='enter_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='exit_date',
            field=models.DateField(null=True),
        ),
    ]