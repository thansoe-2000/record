# Generated by Django 4.0.1 on 2023-04-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_servicedplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedplace',
            name='long_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]