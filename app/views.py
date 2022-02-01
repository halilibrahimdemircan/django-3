from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):

    context = {

        'title': 'Home',
        'dict': {'data': 'data'},
        'list': [1, 2, 3, 4, 5],
    }
    return render(request, 'app/home.html', context)
