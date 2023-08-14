from django.urls import path
from django.conf import settings
from gap.views import Gap

app_name = 'gap'

urlpatterns = [
    path('gap', Gap.as_view(template_name = 'pages/gap_analysis/index.html'), name='gap'),

]