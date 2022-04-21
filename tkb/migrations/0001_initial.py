# Generated by Django 4.0.4 on 2022-04-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('day_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('day_name', models.CharField(max_length=100)),
                ('day_subj', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SubjTask',
            fields=[
                ('subj_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subj_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_subj', models.CharField(max_length=10)),
                ('task_content', models.CharField(max_length=200)),
            ],
        ),
    ]