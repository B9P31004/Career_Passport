# Generated by Django 3.2.6 on 2021-10-24 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211024_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='category_type',
        ),
        migrations.DeleteModel(
            name='CategoryType',
        ),
    ]
