# Generated by Django 4.0.1 on 2023-04-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_personal_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Married',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='personal',
            name='trained_type',
            field=models.ManyToManyField(to='myapp.TrainingType'),
        ),
    ]