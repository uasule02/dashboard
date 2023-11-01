from django.urls import path
from django.conf import settings
from threews.views import MapView, InteractiveMapView, UploadView, ProcessFileView, UploadView1

app_name = 'threews'

urlpatterns = [
    path('interactive', MapView.as_view(template_name = 'pages/threews/index.html'), name='index'),
    path('', InteractiveMapView.as_view(template_name = 'pages/threews/dynamic-map.html'), name='index1'),
    path('upload-file', UploadView.as_view(template_name = 'pages/threews/upload-file.html'), name='upload'),
    path('upload-file1', UploadView1.as_view(template_name = 'pages/threews/upload-demo.html'), name='upload1'),

    path('load-file', ProcessFileView.as_view(template_name = 'pages/threews/load-file.html'), name='load'),



]