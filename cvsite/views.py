from django.shortcuts import render

def section_list(request):
    return render(request, 'cvsite/section_list.html', {})
