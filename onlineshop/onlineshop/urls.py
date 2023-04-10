import onlineshopapp.views as views

"""onlineshop URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from onlineshop.settings import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog', views.show_catalog,name="catalog"),
    path('about_us', views.show_about_us,name="about_us"),
    path('support', views.show_support,name="support"),
    path('', views.show_main,name="main")
]

if DEBUG:
    urlpatterns+=static(MEDIA_URL, document_root=MEDIA_ROOT)