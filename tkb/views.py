from imp import reload
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from .models import SubjTask, Day, Task
import datetime

def index(request):
    today = datetime.date.today()
    weekday = today.weekday()
    listday = Day.objects.all().values()
    listtask = Task.objects.all().values()
    day = listday[weekday]
    listsubj = SubjTask.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'day': day,
        'listsubj': listsubj,
        'weekday': weekday,
        'listtask': listtask,
    }
    return HttpResponse(template.render(context, request))

def addtask(request):
    template = loader.get_template('addtask.html')
    listsubj = SubjTask.objects.all().values()
    listtask = Task.objects.all().values()
    context = {
        'listsubj': listsubj,
        'listtask': listtask,
    }
    return HttpResponse(template.render(context, request))

def addnewtask(request):
    if request.method == 'POST':
        task_subj = request.POST['subj']
        task_content = request.POST['task']
        task = Task(task_subj=task_subj, task_content=task_content)
        task.save()
        return HttpResponseRedirect(reverse('addtask'))
    else:
        return HttpResponseRedirect(reverse('addtask'))

def deletetask(request, task_id):
    task = Task.objects.get(task_id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))

def deletetask_in_addtask(request, task_id):
    task = Task.objects.get(task_id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('addtask')) 

def editschedule(request):
    template = loader.get_template('editschedule.html')
    listsubj = SubjTask.objects.all().values()
    listday = Day.objects.all().values()
    context = {
        'listsubj': listsubj,
        'listday': listday,
    }
    return HttpResponse(template.render(context, request))

def updateschedule(request, id):
  day = Day.objects.get(id=id)
  listsubj = SubjTask.objects.all().values()
  template = loader.get_template('updateschedule.html')
  context = {
    'day': day,
    'listsubj': listsubj,
  }
  return HttpResponse(template.render(context, request))

def updatescheduleprocess(request,id):
    if request.method == 'POST':
        subj_1 = request.POST['subj_1']
        subj_2 = request.POST['subj_2']
        subj_3 = request.POST['subj_3']
        subj_4 = request.POST['subj_4']
        subj_5 = request.POST['subj_5']
        day = Day.objects.get(id=id)
        day.subj_1 = subj_1
        day.subj_2 = subj_2
        day.subj_3 = subj_3
        day.subj_4 = subj_4
        day.subj_5 = subj_5
        day.save()
        return HttpResponseRedirect(reverse('editschedule'))
    else:
        return HttpResponseRedirect(reverse('editschedule'))

def error_404_view(request, exception):
    return render(request, '404.html')



