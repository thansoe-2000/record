# Generated by Django 4.0.6 on 2023-05-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category-photo'),
        ),
    ]