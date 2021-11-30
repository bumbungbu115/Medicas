from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('chatroom', views.chatroom, name = 'chatroom'),
    path('chatroom/<str:inbox>/', views.inbox, name='inbox'),
    path('check', views.check, name='check'),
    path('send', views.send, name='send'),
    path('getmessage/<str:inbox>/', views.getmessage, name='getmessage'),

]