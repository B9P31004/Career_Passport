# Generated by Django 3.2.6 on 2021-12-14 05:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import file_uploader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0010_alter_customuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('event_name', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to=file_uploader.models.save_select_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='%Y-%m-%d-%h-%m-%s')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school')),
            ],
        ),
    ]