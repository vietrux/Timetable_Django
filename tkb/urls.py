from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.addtask, name='addtask'),
    path('addtask/addnewtask', views.addnewtask, name='addnewtask'),
    path('deletetask/<int:task_id>', views.deletetask, name='deletetask'),
    path('addtask/deletetask/<int:task_id>', views.deletetask_in_addtask, name='deletetask_in_addtask'),
    path('editschedule', views.editschedule, name='editschedule'),
    path('updateschedule/<int:id>', views.updateschedule, name='updateschedule'),
    path('updateschedule/updatescheduleprocess/<int:id>', views.updatescheduleprocess, name='updatescheduleprocess'),
]
