# Generated by Django 4.1.2 on 2022-11-10 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_studentassignment_file_alter_favoritecourse_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassignment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
