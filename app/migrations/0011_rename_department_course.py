# Generated by Django 5.0.2 on 2024-03-24 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_department_alter_student_course_delete_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Course',
        ),
    ]
