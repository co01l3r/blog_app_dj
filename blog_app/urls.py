from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.topics, name='topics'),
    path('topic/<str:pk>/', views.topic, name='topic'),
    path('new/', views.topic_create_or_update, name='new'),
    path('update/<str:pk>/', views.topic_create_or_update, name='update'),
    path('delete/<str:pk>/', views.topic_delete, name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
