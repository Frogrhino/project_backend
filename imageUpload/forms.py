import django
from django import forms
from django.forms.fields import FileField
from django.db.models import ImageField


class PictureUploadForm(forms.Form):
    # Create a Django form with a FileField for uploading a picture
    picture = FileField(label='Select a picture')

    # Validate that the file is an image
    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture.name.endswith('.jpg'):
            raise forms.ValidationError('The file must be a JPEG image')
        return picture
