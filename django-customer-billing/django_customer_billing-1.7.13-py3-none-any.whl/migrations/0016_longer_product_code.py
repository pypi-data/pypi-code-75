# Generated by Django 2.1.7 on 2019-02-14 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0015_auto_20181223_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='product_code',
            field=models.CharField(blank=True, db_index=True, help_text='Identifies the kind of product being charged or credited', max_length=20, validators=[django.core.validators.RegexValidator(message='Between 4 and 10 uppercase letters or digits', regex='^[A-Z0-9]{4,10}$')]),
        ),
    ]
