from django.shortcuts import render

def index(request):
    # print('start of homepage views'),
    return render(request, 'homepage/index.html')
