"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from .case_insensitive import CaseInsensitiveConverter
from django.conf import settings
from django.conf.urls.static import static
from landing.views import landing, download_file, WLASL, CV, allprojects
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import include, path

# Register the CaseInsensitiveConverter
register_converter(CaseInsensitiveConverter, 'ci')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("allprojects/", allprojects, name="allprojects"),
    path("WLASL/", WLASL, name="WLASL"),
    path("CV/", CV, name="CV"),
    path("cv/", CV, name="CV"),
    path("download/<str:filename>/", download_file, name="download_file"),
    path("", include("users.urls")),
    path("", include("main.urls")),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
