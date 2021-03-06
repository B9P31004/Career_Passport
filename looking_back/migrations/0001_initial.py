# Generated by Django 3.2.6 on 2021-10-20 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='career_passport02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'career_passport02',
            },
        ),
        migrations.CreateModel(
            name='career_passport03',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'career_passport03',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='名前')),
                ('text', models.CharField(blank=True, max_length=200, verbose_name='テキスト')),
            ],
            options={
                'verbose_name_plural': 'analizing_text',
            },
        ),
        migrations.CreateModel(
            name='career_passport01_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('my_current', models.TextField(verbose_name='今の自分（自分の好きなこと・もの、得意なこと・もの、頑張っていることなど）')),
                ('my_PR', models.TextField(verbose_name='私の自己PR（自分のいところ）')),
                ('my_dream', models.TextField(verbose_name='こんな大人になりたい（将来の夢）')),
                ('getting_skills', models.TextField(verbose_name='そのために、つけたい力')),
                ('study_target', models.TextField(verbose_name='学習面の目標')),
                ('for_study_target', models.TextField(verbose_name='そのために')),
                ('life_target', models.TextField(verbose_name='生活面の目標')),
                ('for_life_target', models.TextField(verbose_name='そのために')),
                ('local_target', models.TextField(verbose_name='家庭・地域での目標')),
                ('for_local_target', models.TextField(verbose_name='そのために')),
                ('others_target', models.TextField(verbose_name='その他（習い事・資格取得）の目標')),
                ('for_others_target', models.TextField(verbose_name='そのために')),
                ('UniqueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'career_passport01_1',
            },
        ),
    ]
