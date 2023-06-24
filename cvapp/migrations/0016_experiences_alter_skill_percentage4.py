# Generated by Django 4.2.2 on 2023-06-24 13:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0015_alter_skill_percentage3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name=' Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('company_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ('start_date',),
            },
        ),
        migrations.AlterField(
            model_name='skill',
            name='percentage4',
            field=models.IntegerField(blank=True, default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage4'),
        ),
    ]
