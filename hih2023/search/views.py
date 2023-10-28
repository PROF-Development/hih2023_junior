from django.shortcuts import render
# import models as model
import search.processing_modules as function


def search(request):
    template = 'search/search.html'
    context = {"documents": None}
    if request.method == "POST":
        print(request.POST)
        context["documents"] = function.get_documents(request.POST.dict())
        print(context["documents"], '-------')
        for document in context["documents"].keys():
            print(context["documents"][document], "test")



    return render(request, template, context)
