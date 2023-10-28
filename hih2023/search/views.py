from django.shortcuts import render
# import models as model
import search.processing_modules as function


def index(request):
    template = 'search/index.html'
    context = {"documents": None}
    if request.method == "POST":
        context["documents"] = function.get_documents(request.POST.dict())

    return render(request, template, context)
