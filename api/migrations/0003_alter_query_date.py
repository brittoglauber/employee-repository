# Generated by Django 4.2.2 on 2023-06-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_query_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
