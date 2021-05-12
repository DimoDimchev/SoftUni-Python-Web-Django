from os.path import join, isfile

from django.conf import settings
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
        return render(request, 'resources/pets.html', context)
    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets')
        else:
            context = {
                'pets': Pet.objects.all(),
                'form': form,
            }

            return render(request, 'resources/pets.html', context)


def serve_private_files(request, path):
    full_path = join(settings.MEDIA_ROOT, 'private', path)
    if isfile(full_path):
        pass
    return None
