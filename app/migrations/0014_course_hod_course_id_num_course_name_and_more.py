# Generated by Django 5.0.2 on 2024-03-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hod',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='id_num',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=True, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='num_student',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
