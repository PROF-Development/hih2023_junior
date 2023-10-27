from django.shortcuts import render


def index(request):
    template = 'search/index.html'
    return render(request, template)
