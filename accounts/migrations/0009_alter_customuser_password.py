# Generated by Django 3.2.6 on 2021-12-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.TextField(help_text='パスワードを入力', max_length=12),
        ),
    ]