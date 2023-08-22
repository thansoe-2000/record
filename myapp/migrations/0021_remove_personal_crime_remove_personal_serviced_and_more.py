# Generated by Django 4.0.1 on 2023-04-04 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='crime',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='serviced',
        ),
        migrations.AddField(
            model_name='personal',
            name='long_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.gender'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='join_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='married',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.married'),
        ),
    ]