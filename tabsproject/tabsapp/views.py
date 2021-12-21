from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'site_title': 'Tabs App'}
    return render(request, 'tabsapp/index.html', context)
