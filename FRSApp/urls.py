from django.urls import path
from .views import upload_image, success_view

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('success/<str:name>/', success_view, name='success'),
]
