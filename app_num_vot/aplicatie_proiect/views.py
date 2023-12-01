from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract as tess
from .forms import UploadFileForm
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Users\Tudor\AppData\Local\Programs\Tesseract-OCR\tesseract'
# Create your views here.

def index(response):
   return render(response, "aplicatie_proiect/home.html",{}) 



def citit_img(request):
    context = {}
    image_text = "None"
    context.update({'image_text':image_text})
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            image_text = tess.image_to_string(image)

            context.update({'image_text': image_text})
            form = UploadFileForm()  # Reset the form after processing

    else:
        form = UploadFileForm()

    context.update({'form': form})
    
    return render(request, "aplicatie_proiect/templ_img.html", context)