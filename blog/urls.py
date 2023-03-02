from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name = "HomePage"),
    path('blog_page/<str:pk>',views.room, name="blogs"),
    path('create-blog/',views.createRoom,name="create-blog"),
    path('update-blog/<str:pk>',views.updateRoom,name='update-blog'),
    path('delete-blog/<str:pk>',views.deleteRoom,name='delete-blog'),
    path('delete-comment/<str:pk>',views.deleteMessage,name='delete-comment'),
    path('blogger/<str:pk>',views.profilePage,name='blogger'),
    path('update-user/',views.editUser,name='update-blogger'),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)