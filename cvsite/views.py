from django.shortcuts import render
from .models import Section
from django.shortcuts import render, get_object_or_404
from .forms import SectionForm
from django.shortcuts import redirect

def component_list(request):
    list = Section.objects.order_by('id')
    return render(request, 'component_list.html', {'list': list})

def component_detail(request, pk):
    component = get_object_or_404(Section, pk=pk)
    return render(request, 'component_detail.html', {'component': component})

def component_edit(request, pk):
    component = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = SectionForm(request.POST, instance=component)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('component_list', pk=component.pk)
    else:
        form = SectionForm(instance=component)
    return render(request, 'component_edit', {'form': form})