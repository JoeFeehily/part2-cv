from django.shortcuts import render

def mainsite(request):
    return render(request, 'mainsite.html', {})
