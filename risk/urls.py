from django.urls import path
from django.conf import settings
from risk.views import Risk

app_name = 'risk'

urlpatterns = [
    path('risk', Risk.as_view(template_name = 'pages/risk_analysis/index.html'), name='risk'),

]