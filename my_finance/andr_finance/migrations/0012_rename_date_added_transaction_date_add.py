# Generated by Django 5.0.3 on 2024-03-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andr_finance', '0011_alter_account_name_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date_added',
            new_name='date_add',
        ),
    ]