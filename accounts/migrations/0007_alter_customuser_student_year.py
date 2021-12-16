# Generated by Django 3.2.6 on 2021-11-04 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211024_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_year',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]