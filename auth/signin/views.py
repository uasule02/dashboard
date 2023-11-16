from django.views.generic import TemplateView
from django.conf import settings
from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to urls.py file for more pages.
"""

class AuthSigninView(TemplateView):
    template_name = 'pages/auth/signin.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # A function to init the global layout. It is defined in _keenthemes/__init__.py file
        context = KTLayout.init(context)

        if self.request.method == 'POST':
            username = self.request.POST['username']
            password = self.request.POST['password']
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                messages.success(self.request, 'You have successfully logged in.')
                return (user)  # Replace 'dashboard' with the URL name of your dashboard page.
            else:
                messages.error(self.request, 'Invalid login credentials.')

        context.update({
            'layout': KTTheme.setLayout('auth.html', context),
        })

        return context
