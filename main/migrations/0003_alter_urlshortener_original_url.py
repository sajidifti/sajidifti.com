# Generated by Django 4.1.7 on 2024-02-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='original_url',
            field=models.URLField(),
        ),
    ]