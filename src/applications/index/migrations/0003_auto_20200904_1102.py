# Generated by Django 3.1.1 on 2020-09-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200904_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='prices',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cake_name',
            name='ingredients',
            field=models.TextField(max_length=300, verbose_name='Описание ингредиентов'),
        ),
    ]
