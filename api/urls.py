from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('topics/', views.get_topics),
    path('topics/<str:pk>/', views.get_topic),
]
