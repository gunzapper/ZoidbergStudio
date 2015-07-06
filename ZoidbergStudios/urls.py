"""ZoidbergStudios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^$', 'dicom_visio.views.home_page', name='home'),
     url(r'^dicom_visio/(\d+)/$', 'dicom_visio.views.view_dicom', name='view_dicom'),
     url(r'^dicom_visio/(\d+)/add_datum$', 'dicom_visio.views.add_datum', name='add_datum'),
     url(r'^dicom_visio/new$', 'dicom_visio.views.new_dicom', name='new_dicom')
    #url(r'^admin/', include(admin.site.urls)),
]
