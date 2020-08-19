from django.shortcuts import render


def index(request):
    return render(request, 'index/cake_index.html')
