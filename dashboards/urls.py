from django.urls import path
from django.conf import settings
from dashboards.views import DashboardsView, Three3ws

app_name = 'dashboards'

urlpatterns = [
    path('', DashboardsView.as_view(template_name = 'pages/dashboards/index.html'), name='index'),
    path('threews/', Three3ws.as_view(template_name = 'pages/dashboards/3ws.html'), name='threews'),

    path('error', DashboardsView.as_view(template_name = 'non-exist-file.html'), name='Error Page'),
]