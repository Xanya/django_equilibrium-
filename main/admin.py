from django.contrib import admin

from .models import MainPageContent
from image_cropping import ImageCroppingMixin

@admin.register(MainPageContent)
class MainPageContentAdmin(ImageCroppingMixin, admin.ModelAdmin):
    #disable the button if object already exists
    def has_add_permission(self, request):
        return not MainPageContent.objects.exists()
