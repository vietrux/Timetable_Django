# Generated by Django 4.0.4 on 2022-04-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkb', '0005_delete_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=100)),
                ('subj_1', models.CharField(max_length=10)),
                ('subj_2', models.CharField(max_length=10)),
                ('subj_3', models.CharField(max_length=10)),
                ('subj_4', models.CharField(max_length=10)),
                ('subj_5', models.CharField(max_length=10)),
            ],
        ),
    ]