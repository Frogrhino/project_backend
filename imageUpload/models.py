from django.db import models


class imageUpload(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Picture(models.Model):
    file = models.ImageField()
    caption = models.CharField(max_length=255)
