from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage, FileSystemStorage
from django.shortcuts import render

from .models import imageUpload
from .models import Picture
from .forms import PictureUploadForm


class HomePageView(ListView):
    model = imageUpload
    template_name = "home.html"


def upload_picture(request):
    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES)

        if form.is_valid():
            fs = FileSystemStorage(
                location='media/uploaded_images')
            picture = form.cleaned_data['picture']
            filename = fs.save(
                'uploaded_images/' + picture.name, picture)
            # Save the picture to a file
            with fs.open(filename, 'wb') as f:
                for chunk in picture.chunks():
                    f.write(chunk)

            # Save the picture to the database
            picture_model = Picture(file=picture, caption=picture.name)
            picture_model.save()
            return HttpResponseRedirect('/success/')

    else:
        form = PictureUploadForm()

    return render(request, 'upload_picture.html', {'form': form})


def success_view(request):
    picture = Picture.objects.last()
    return render(request, 'success.html', {'picture': picture})
