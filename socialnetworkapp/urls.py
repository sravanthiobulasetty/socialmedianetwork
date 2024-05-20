from django.urls import path
from . import views

urlpatterns = [
     path('',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('edit_profile',views.edit_profile,name='edit_profile'),
     path('change password',views.change_password,name='change_password'),
     path('view profile', views.view_profile, name='view_profile'),
]