# Generated by Django 5.0.6 on 2024-07-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='updated_by',
            field=models.CharField(blank=True, default='No Update Yet', max_length=100, null=True),
        ),
    ]
