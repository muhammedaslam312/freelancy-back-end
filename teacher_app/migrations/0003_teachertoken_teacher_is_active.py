# Generated by Django 4.1.2 on 2022-10-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
