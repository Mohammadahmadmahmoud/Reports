from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.main, name='home'),
    path('announcement/', views.announcement, name='announcement'),
    path('create_order/str:pk',views.create_order, name='create_order'),
    path('customer/<str:pk>', views.customer , name ='customer'),
    path('update_announcement/<str:pk>', views.update_announcement, name='update_announcement'),
    path('delete_announcement/<str:pk>', views.delete_announcement, name='delete_announcement'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/<str:pk>', views.customer, name ='customer'),
    path('orders/', views.orders, name ='orders'),
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name ='Login'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
