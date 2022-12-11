from django.urls import path

from .views import HomePageView
from .views import upload_picture, success_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('upload-picture/', upload_picture, name='upload_picture'),
    path('success/', success_view)
]
