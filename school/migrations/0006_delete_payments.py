# Generated by Django 4.2.2 on 2024-08-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_payments_summ'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
