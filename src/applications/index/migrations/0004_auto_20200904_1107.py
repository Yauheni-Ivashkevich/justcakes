# Generated by Django 3.1.1 on 2020-09-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200904_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='prices',
            field=models.TextField(blank=True, null=True, verbose_name='Стоимость и заказ'),
        ),
    ]