# Generated by Django 4.2.2 on 2023-06-23 03:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0008_alter_skill_backendname_alter_skill_devopsname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.IntegerField(blank=True, default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage'),
        ),
    ]