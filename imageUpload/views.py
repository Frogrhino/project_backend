from django.views.generic import ListView
from .models import imageUpload


class HomePageView(ListView):
    model = imageUpload
    template_name = "home.html"
