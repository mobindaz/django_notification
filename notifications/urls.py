from django.urls import path
from . import views
from .views import admin_dashboard, edit_notification, delete_notification

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('add-notification/', views.add_notification, name='add_notification'),
     path('admin/', admin_dashboard, name='admin_dashboard'),
    path('admin/edit/<int:pk>/', edit_notification, name='edit_notification'),
    path('admin/delete/<int:pk>/', delete_notification, name='delete_notification'),
]
