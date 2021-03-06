# Generated by Django 2.0.1 on 2018-11-06 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('qty', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('tax', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_order', to='service.Order')),
            ],
        ),
    ]
