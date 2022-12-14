# Generated by Django 4.1.2 on 2022-11-10 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0009_alter_chapter_course'),
        ('main', '0011_alter_studentassignment_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.course'),
        ),
        migrations.AlterField(
            model_name='favoritecourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
