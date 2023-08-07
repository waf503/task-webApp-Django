
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/completed', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('login/',views.signin, name='signin'),
    path('task/create',views.taskCreate, name='task_create'),
    path('tasks/<int:task_id>/',views.taskDetail, name='task_detail'),
    path('tasks/<int:task_id>/complete',views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/uncomplete',views.uncomplete_task, name='uncomplete_task'),
    path('tasks/<int:task_id>/delete',views.delete_task, name='delete_task'),

]
