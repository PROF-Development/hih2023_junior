from django.shortcuts import render


def index(request):
    context = {'docs': None}
    template = 'search/index.html'
    if request.method == "POST":
        form = request.POST.dict()
        context['docs'] = form['input_field']
        # print(form['input_field'].value())
        print(form['input_field'])
        return render(request, template, context)
    else:
        return render(request, template)
