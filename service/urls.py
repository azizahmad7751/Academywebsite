from django.urls import path
from .import views


urlpatterns = [
    path('', views.service_page, name='service'),
    path('services_details/<int:id>', views.services_details, name='services_details'),
    #path('students/', views.students, name='students'),
   
]
