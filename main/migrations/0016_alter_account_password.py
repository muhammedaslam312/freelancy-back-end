# Generated by Django 4.1.2 on 2022-11-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_studentassignment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]