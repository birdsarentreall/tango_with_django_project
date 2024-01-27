from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # dict construction to pass to template engine as its context
    # key boldmessage matches to {{boldmessage}} in template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # return rendered responce to send to client
    # use of shortcut function
    # first parameter is the template we want to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Michael Liang.'}

    return render(request, 'rango/about.html', context=context_dict)