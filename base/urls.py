from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name = "Home"),
    path('room_page/<str:pk>',views.room, name="Rooms"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('delete-message/<str:pk>',views.deleteMessage,name='delete-message'),
    path('profile/<str:pk>',views.profilePage,name='profile'),
    path('update-user/',views.editUser,name='update-user'),
    path('index/',views.indexPage ,name="index"),
    path('to-do/',include('focuzz.urls')),
    path('blog/',include('blog.urls')),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)