# Generated by Django 4.2.2 on 2023-06-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0009_alter_skill_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.IntegerField(blank=True, default=50, verbose_name='Percentage'),
        ),
    ]