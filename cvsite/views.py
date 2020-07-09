from django.shortcuts import render
from .models import Section

def mainsite(request):
    list = Section.objects.order_by('id')
    return render(request, 'mainsite.html', {'list': list})
