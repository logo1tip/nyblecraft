# Generated by Django 4.0.1 on 2022-01-17 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_department', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_position', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255)),
                ('device_date', models.DateField()),
                ('current_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.department')),
                ('current_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.position')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
                'db_table': 'worker',
            },
        ),
    ]
