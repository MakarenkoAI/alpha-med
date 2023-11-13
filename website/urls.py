from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search, name='search'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('room/', views.room, name='room'),
    path('one_room/<int:pk>', views.one_room, name='one_room'),
    path('delete_room/<int:pk>', views.delete_room, name='delete_room'),
    path('add_room/', views.add_room, name='add_room'),
    path('update_room/<int:pk>', views.update_room, name='update_room'),
    path('new1/', views.new1, name='new1'),
    path('new2/', views.new2, name='new2'),
    path('new3/', views.new3, name='new3'),
]
