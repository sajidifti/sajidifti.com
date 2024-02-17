from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http.response import HttpResponse
import os
import mimetypes

# Create your views here.


def landing(request):
    return HttpResponse("New Porfolio is in Developent. Will be available very shortly.")


def CV(request):
    return render(request, 'CV.html')


def WLASL(request):
    return render(request, 'WLSLT.html')


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
