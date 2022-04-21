from django.db import models

class SubjTask(models.Model):
    subj_code = models.CharField(max_length=10,primary_key=True)
    subj_name = models.CharField(max_length=100)

class Day(models.Model):
    day_name = models.CharField(max_length=100)
    subj_1 = models.CharField(max_length=10)
    subj_2 = models.CharField(max_length=10)
    subj_3 = models.CharField(max_length=10)
    subj_4 = models.CharField(max_length=10)
    subj_5 = models.CharField(max_length=10)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_subj = models.CharField(max_length=10)
    task_content = models.CharField(max_length=200)



