# Generated by Django 5.0.3 on 2024-03-26 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andr_finance', '0003_remove_transaction_change_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='description',
        ),
    ]