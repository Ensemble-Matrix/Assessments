from django.db import models
from django.utils.safestring import mark_safe

class Imager(models.Model):
    def upload_path(instance, filename):
        return '/images/'.join([filename])
    actual_label = models.CharField(max_length=100)
    predicted_label = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path, blank=True)
    def show_image(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    show_image.short_description = 'Image'
    show_image.allow_tags = True

    def __str__(self):
        return self.actual_label
