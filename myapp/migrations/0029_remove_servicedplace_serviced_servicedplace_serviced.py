# Generated by Django 4.0.1 on 2023-04-27 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_remove_servicedplace_serviced_servicedplace_serviced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedplace',
            name='serviced',
        ),
        migrations.AddField(
            model_name='servicedplace',
            name='serviced',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.department'),
        ),
    ]
