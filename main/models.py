from django.db import models

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField, ImageCropField


class MainPageContent(models.Model):
    header_image = ImageCropField(verbose_name="Header image", upload_to="header/")
    crop_header_image = ImageRatioField('header_image', '500x500')
    title = models.CharField(
        verbose_name="Title on the main page",
        max_length=500,
        blank=False,
        null=False
    )
    content = RichTextField(
        verbose_name="Text on the main page",
        blank=False,
        null=False
    )
    
    class Meta:
        verbose_name = "Main page content"
        verbose_name_plural = "Main page content"
        
    def __str__(self):
        return self.title
    