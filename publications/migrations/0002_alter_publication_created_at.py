# Generated by Django 5.0.6 on 2024-06-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de criação'),
        ),
    ]