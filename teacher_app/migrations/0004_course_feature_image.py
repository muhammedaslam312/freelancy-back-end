# Generated by Django 4.1.2 on 2022-10-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0003_teachertoken_teacher_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='feature_image',
            field=models.ImageField(blank=True, upload_to='photos/course_image/'),
        ),
    ]
