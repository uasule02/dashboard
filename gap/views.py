from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from pprint import pprint

# Create your views here.


class Gap(TemplateView):
    template_name = 'pages/gap_analysis/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add your additional context data here if needed
        context = KTLayout.init(context)

        # Include vendors and javascript files for dashboard widgets

        return context