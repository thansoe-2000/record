# Generated by Django 4.0.6 on 2023-03-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_trainingground'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]