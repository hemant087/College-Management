# Generated by Django 5.0.2 on 2024-03-28 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_hod_course_dept_hod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'TEACHER'), (3, 'STUDENT')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=100)),
                ('Qualification', models.TextField()),
                ('Experience', models.TextField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
