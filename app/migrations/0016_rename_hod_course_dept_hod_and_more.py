# Generated by Django 5.0.2 on 2024-03-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_student_registration_alter_student_roll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='hod',
            new_name='dept_hod',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='id_num',
            new_name='dept_id',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='dept_name',
        ),
    ]
