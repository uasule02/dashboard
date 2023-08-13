from django.urls import path
from django.conf import settings
from threews.views import MapView

app_name = 'threews'

urlpatterns = [
    path('', MapView.as_view(template_name = 'pages/threews/index.html'), name='index'),

]