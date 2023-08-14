from django.urls import path
from django.conf import settings
from funding.views import Funding

app_name = 'funding'

urlpatterns = [
    path('funding', Funding.as_view(template_name = 'pages/funding/index.html'), name='funding'),

]