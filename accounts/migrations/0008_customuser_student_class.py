# Generated by Django 3.2.6 on 2021-11-07 09:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='student_class',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
