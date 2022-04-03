from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login_page/', views.login_page, name='login_page'),
]