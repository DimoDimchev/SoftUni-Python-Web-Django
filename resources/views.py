from django.shortcuts import render, redirect

# Create your views here.
from resources.forms import PetForm
from resources.models import Pet


def resources(request):
    if request.method == 'GET':
        context = {
            'pets': Pet.objects.all(),
            'form': PetForm
        }
        return render(request, 'resources/index.html', context)
    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets')

        context = {
            'pets': Pet.objects.all(),
            'form': form,
        }

        return render(request, 'resources/index.html', context)
