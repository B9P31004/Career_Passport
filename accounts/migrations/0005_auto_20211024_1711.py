# Generated by Django 3.2.6 on 2021-10-24 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211024_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school_ID',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_ID',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='school_ID',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_ID',
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
