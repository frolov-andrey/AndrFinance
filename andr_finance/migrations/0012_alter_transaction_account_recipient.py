# Generated by Django 5.0.2 on 2024-02-28 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_finance', '0011_alter_transaction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_recipient', to='andr_finance.account'),
        ),
    ]
