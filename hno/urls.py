from django.urls import path
from django.conf import settings
from hno.views import Hno

app_name = 'hno'

urlpatterns = [
    path('hno', Hno.as_view(template_name = 'pages/hno/index.html'), name='hno'),

]