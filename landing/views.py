from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')


def CV(request):
    return render(request, 'CV.html')


def WLASL(request):
    return render(request, 'WLSLT.html')


def sign(request):
    return redirect('https://github.com/sajidifti/Word_Level_Sign_Language_Translator_Django_OpenCV_Local')

def silicon(request):
    return redirect('https://github.com/sajidifti/Siliconbyte_Bangla_Tech_News_Site_PHP')

def rent(request):
    return redirect('https://github.com/sajidifti/RentMatch_To-Let_Platform')


def download_file(request, filename):
    context = {'filename': filename}

    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'download.html', context)
