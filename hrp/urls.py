from django.urls import path
from django.conf import settings
from hrp.views import Hrp

app_name = 'hrp'

urlpatterns = [
    path('hrp', Hrp.as_view(template_name = 'pages/hrp/index.html'), name='hrp'),

]