from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        # Get the host from the request object
        host = request.get_host()

        # Check if the host is a local host
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0

        # Create a context dictionary containing the installed apps and local host status
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }

        # Render the main.html template with the context data
        return render(request, 'home/main.html', context)
