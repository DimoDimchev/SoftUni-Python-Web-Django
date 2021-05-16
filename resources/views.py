from os.path import join, isfile

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.decorators import group_required
from resources.forms import PetForm
from resources.models import Pet


@login_required
# @group_required(groups=['Regular user'])
def resources(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        for pet in pets:
            pet.can_delete = pet.created_by_id == request.user.id
        context = {
            'pets': pets,
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


def serve_private_files(request):
    path = 'documents/shortcuts.txt'
    full_path = join(settings.MEDIA_ROOT, 'private', path)
    if isfile(full_path):
        file = open(path, 'rb')
        response = HttpResponse(content=file)
        response['Content-Disposition'] = 'attachment'
        return response
    return None
