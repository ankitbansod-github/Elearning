from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/english/', views.english, name='english'),
    path('courses/math/', views.math, name='math'),
    path('contact/', views.contact, name='contact'),


]