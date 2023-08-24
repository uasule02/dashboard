from django.urls import path
from django.conf import settings
from threews.views import MapView, InteractiveMapView

app_name = 'threews'

urlpatterns = [
    path('interactive', MapView.as_view(template_name = 'pages/threews/index.html'), name='index'),
    path('', InteractiveMapView.as_view(template_name = 'pages/threews/dynamic-map.html'), name='index1'),


]