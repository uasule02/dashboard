from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.urls import resolve
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from pprint import pprint
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from django.views.generic import TemplateView
from django.http import HttpResponse
from io import BytesIO
import base64



