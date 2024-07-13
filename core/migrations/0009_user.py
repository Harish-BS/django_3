# Generated by Django 5.0.6 on 2024-07-13 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('client_id', models.ForeignKey(default='No ID', on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('department_id', models.ForeignKey(default='No ID', on_delete=django.db.models.deletion.CASCADE, to='core.department')),
                ('designation_id', models.ForeignKey(default='No ID', on_delete=django.db.models.deletion.CASCADE, to='core.designation')),
            ],
        ),
    ]
