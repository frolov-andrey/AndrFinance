# Generated by Django 4.1.13 on 2024-04-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("andr_finance", "0006_transaction_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
