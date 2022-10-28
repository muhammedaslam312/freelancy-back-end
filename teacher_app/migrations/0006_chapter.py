# Generated by Django 4.1.2 on 2022-10-27 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0005_course_used_techs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('video', models.FileField(blank=True, upload_to='videos/chapter_videos/')),
                ('remark', models.TextField(blank=True)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_app.course')),
            ],
            options={
                'verbose_name_plural': '4. Chapters',
            },
        ),
    ]
