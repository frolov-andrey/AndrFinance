# Generated by Django 5.0.2 on 2024-02-28 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andr_finance', '0005_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='level',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
    ]
