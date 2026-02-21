from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('upload/', views.upload_outfit, name='upload_outfit'),
    path('gallery/', views.style_gallery_view, name='outfit_list'),
    path('delete/<int:outfit_id>/', views.delete_outfit, name='delete_outfit'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('result/<int:outfit_id>/', views.outfit_result_view, name='outfit_result'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
