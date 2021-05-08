from django.shortcuts import render

# Create your views here.
from resources.models import Pet


def resources(request):
    context = {
        'pets': Pet.objects.all()
    }

    return render(request, 'resources/index.html', context)
