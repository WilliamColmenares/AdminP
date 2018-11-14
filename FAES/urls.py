"""FAES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from actas.views import login_page, logout_page
from django.conf import settings
# from actas.views import ActasDetailView, upload_acta_page
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', login_page),
	path('salir/', logout_page, name='logout'),
	# path('principal/', dashboard_page),
	# path('agregar/', upload_acta_page),
	# re_path(r'^detalle/(?P<pk>\d+)/$', ActasDetailView.as_view()),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
