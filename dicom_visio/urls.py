
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^(\d+)/$', 'dicom_visio.views.view_dicom', name='view_dicom'),
     url(r'^(\d+)/add_datum$', 'dicom_visio.views.add_datum', name='add_datum'),
     url(r'^new$', 'dicom_visio.views.new_dicom', name='new_dicom')
    #url(r'^admin/', include(admin.site.urls)),
]
