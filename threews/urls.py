from django.urls import path
from django.conf import settings
from threews.views import MapView, InteractiveMapView, UploadView, ProcessFileView, UploadView1 #load_months

app_name = 'threews'

urlpatterns = [
    path('interactive', MapView.as_view(template_name = 'pages/threews/index.html'), name='index'),
    path('', InteractiveMapView.as_view(template_name = 'pages/threews/dynamic-map.html'), name='index1'),
    path('upload', UploadView.as_view(template_name = 'pages/threews/upload-sample.html'), name='upload1'),
    path('upload-file', UploadView1.as_view(template_name = 'pages/threews/upload-demo.html'), name='upload'),
    path('load-file', ProcessFileView.as_view(template_name = 'pages/threews/load-demo.html'), name='load'),
    #path('load_months/', load_months, name='load_months'),



]