from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', {})


def list_view(request):
    return render(request, 'blog/list.html', {})
