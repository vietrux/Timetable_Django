# Generated by Django 4.0.4 on 2022-04-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkb', '0003_day_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_subj', models.CharField(max_length=10)),
                ('task_content', models.CharField(max_length=200)),
            ],
        ),
    ]
