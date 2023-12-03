from django.shortcuts import render
from django.http import HttpResponse
import pytesseract as tess
from PIL import Image as PilImage 
from .forms import ImageUploadForm
import uuid
import os

tess.pytesseract.tesseract_cmd = r'C:\Users\Tudor\AppData\Local\Programs\Tesseract-OCR\tesseract'
# Create your views here.

def index(response):
   return render(response, "aplicatie_proiect/home.html",{}) 


def upload_image(request):
    extracted_text="Asteptam"
    image_path = r'C:\Users\Tudor\Desktop\aplicatie_lucru\app_num_vot\uploaded_images/'  # Replace this with the correct path
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form to get the instance
            instance = form.save(commit=False)

            # Generate a unique filename
            unique_filename = f"{uuid.uuid4().hex}.png"

            # Set the image field to the unique filename
            instance.image.name = unique_filename

            # Save the form with the updated image field
            instance.save()

            # Now that the image is saved, get its path and perform OCR
            image_path = os.path.join(r'C:\Users\Tudor\Desktop\aplicatie_lucru\app_num_vot\uploaded_images', unique_filename)
            extracted_text = tess.image_to_string(PilImage.open(image_path))

            # Process or display the extracted text as needed
    else:
        form = ImageUploadForm()
    

   
    
    return render(request, "aplicatie_proiect/templ_img.html", {'image_text':extracted_text })
