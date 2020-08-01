from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors, name='doctors'),
    path('news/', views.news, name='news'),
    path('newsdetail/', views.newsdetail, name='newsdetail'),
    path('gallery/', views.gallery, name='gallery'),
    
    # path('test/', views.appointment_form_view,
    #      name='appointment_form_view'),
]