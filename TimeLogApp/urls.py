from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('grid', views.grid_view, name='grid_view'),
    path('api/users/', views.user_data_api, name='user_data_api'),
    path('create-user/', views.create_user, name='create_user'),
]
