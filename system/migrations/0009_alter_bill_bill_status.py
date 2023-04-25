# Generated by Django 4.2 on 2023-04-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=10),
        ),
    ]
