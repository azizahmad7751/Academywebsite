from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio'),
    path(r'portfolio_details/<int:portfolio_id>/', views.portfolio_details, name='portfolio-details')
]
