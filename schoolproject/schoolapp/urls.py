from . import views
from django.urls import path
app_name='schoolapp'


urlpatterns = [
    path('', views.demo, name='demo'),
    path('all-courses/', views.all_courses, name='all_courses'),
    path('form/', views.formr, name='form'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('credentials/logout', views.logout, name='logout'),
]

