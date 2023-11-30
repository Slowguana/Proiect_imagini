from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract
from .forms import UploadFileForm
# Create your views here.

def index(response):
   return render(response, "aplicatie_proiect/home.html",{}) 



def citit_img(request):
    context = dict()
    image_text=None
    # Windows users need to add something like:
    # pytesseract.pytesseract.tesseract.cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            image = Image.open(request.FILES['file_upload'])
            image_text = pytesseract.image_to_string(image)
            # If you were handling larger files, perhaps something like this would be better
            # with tempfile.TemporaryFile() as temp_file:
            #     for chunk in request.FILES['file_upload'].chunks():
            #         temp_file.write(chunk)
            #     image = Image.open(temp_file)
            #     image_text = pytesseract.image_to_string(image)

            context.update({'image_text': image_text, })
            # reset the form: typically we'd redirect elsewhere to prevent multiple
            # submissions of data, but there is no database interaction here - only
            # sending the text back
            form = UploadFileForm()
    else:
        form = UploadFileForm()

    context.update({'form': form, })
    
    return render(request, "aplicatie_proiect/templ_img.html", {"image_text":context[form]})