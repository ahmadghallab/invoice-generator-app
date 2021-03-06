# Generated by Django 2.0.1 on 2018-11-06 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20181106_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('vehicle_counter', models.IntegerField(blank=True, null=True)),
                ('complain', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='service.Customer')),
            ],
        ),
    ]
