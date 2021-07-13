from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct dict to pass to the template engine as context:
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # return rendered response to a client
    # first param is template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')