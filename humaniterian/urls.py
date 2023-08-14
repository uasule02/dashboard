from django.urls import path
from django.conf import settings
from humaniterian.views import Humaniterian

app_name = 'humaniterian'

urlpatterns = [
    path('humaniterian', Humaniterian.as_view(template_name = 'pages/humaniterian/index.html'), name='humaniterian'),

]