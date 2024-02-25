from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http.response import HttpResponse
import os
import mimetypes
from django.contrib import messages
from .models import Project
from .forms import ContactForm
from users.views import notificationEmail


# Create your views here.


def landing(request):
    allerrors = ""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message_from_user = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            notificationEmail(request, f"{form.cleaned_data['name']} - SajidIfti.Com",
                              message_from_user, "info@sajidifti.com", sender_name = "Portfolio")
            messages.success(request, f"Thank You for Contacting Me.\nI'll Get Back to You As Soon As Possible.")
            return redirect("landing")
        else:
            for field, error_messages in form.errors.items():
                for error_message in error_messages:
                    if (
                        field == "captcha"
                        and error_message == "This field is required."
                    ):
                        custom_error_message = "You must pass the reCAPTCHA test. "
                        allerrors = allerrors + " " + custom_error_message
                    else:
                        allerrors = allerrors + " " + error_message
            messages.error(request, allerrors)
            return redirect("landing")
    else:
        form = ContactForm()

    projects = Project.objects.order_by("-priority")[:6]

    return render(request, "landing/index.html", {"projects": projects, "form": form})


def allprojects(request):
    projects = Project.objects.order_by("-priority")
    return render(request, "landing/allprojects.html", {"projects": projects})


def CV(request):
    return render(request, "CV.html")


def WLASL(request):
    return render(request, "WLSLT.html")


def download_file(request, filename):
    context = {"filename": filename}

    if filename != "":
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + "/files/" + filename
        # Open the file for reading content
        path = open(filepath, "rb")
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response["Content-Disposition"] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, "download.html", context)
