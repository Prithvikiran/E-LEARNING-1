from django.urls import path,include
from base.views import indexPage

from . import views

urlpatterns = [
    path('', views.index, name='to_do'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('start-task',views.startTask,name="timer"),
    path('blog/',include('blog.urls')),
    path('menu/',indexPage),
]
