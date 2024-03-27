# Generated by Django 5.0.3 on 2024-03-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andr_finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='change',
            field=models.CharField(choices=[('minus', 'Расход'), ('plus', 'Доход'), ('transfer', 'Перевод')], default='minus', max_length=20, verbose_name='Тип транзакции 2'),
        ),
    ]