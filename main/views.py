from django.shortcuts import render

from .models import MainPageContent

# Create your views here.
def index(request):
    main_content = MainPageContent.objects.first()
    
    if not main_content:
        context = {
            "header_image": None,
            "title": "Set proper title from the admin page.",
            "content": "Set proper content from the admin page"
        }
    else:
        context = {
            "header_image": main_content.header_image,
            "title": main_content.title,
            "content": main_content.content,
            "cropped_image": main_content.crop_header_image,
        }
        
    return render(request, "index.html", context=context)