# Generated by Django 3.2.6 on 2021-11-04 12:56

from django.db import migrations, models
import grade_management.models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='regular_test',
            field=models.CharField(choices=[('中間', '中間'), ('期末', '期末')], max_length=2, validators=[grade_management.models.check_regular_test], verbose_name='中間または期末'),
        ),
    ]