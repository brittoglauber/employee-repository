# Generated by Django 4.2.2 on 2023-06-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='employee_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
