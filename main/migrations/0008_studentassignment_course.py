# Generated by Django 4.1.2 on 2022-11-09 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0009_alter_chapter_course'),
        ('main', '0007_studentassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher_app.course'),
        ),
    ]