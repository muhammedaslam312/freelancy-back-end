# Generated by Django 4.1.2 on 2022-10-27 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_app', '0006_chapter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='Course',
            new_name='course',
        ),
    ]
