# Generated by Django 2.0.1 on 2018-01-20 17:35

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_add_product_code_and_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=django_fsm.FSMField(choices=[('PENDING', 'Pending'), ('PAST_DUE', 'Past-due'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], db_index=True, default='PENDING', max_length=20),
        ),
    ]
