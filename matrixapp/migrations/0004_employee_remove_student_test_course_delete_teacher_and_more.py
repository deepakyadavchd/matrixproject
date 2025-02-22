# Generated by Django 5.0.7 on 2024-09-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixapp', '0003_course_student_test_delete_student_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=70)),
                ('gender', models.CharField(max_length=50)),
                ('hobby', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='student_test',
            name='course',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student_test',
        ),
    ]
