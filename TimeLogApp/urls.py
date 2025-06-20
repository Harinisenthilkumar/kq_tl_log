from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('timelog/', views.home, name='home'),
    path('grid/', views.grid_view, name='grid_view'),
    path('api/users/', views.user_data_api, name='user_data_api'),
    path('create-user/', views.create_user, name='create_user'),
    path('api/users/<int:user_id>/', views.get_user_detail),
    path('users/update/<int:user_id>/', views.update_user),
    path('users/delete/<int:user_id>/', views.delete_user),
]
