from django.shortcuts import render
from django.views.generic.base import View, TemplateView

from resources.models import Pet


class IndexView(View):
    def get(self, request):
        context = {
            'heading_text': 'Hello from base View',
            'pets': Pet.objects.all(),
        }

        return render(request, 'cbv/index.html', context)

    def post(self, request):
        pass


class IndexTemplateView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['heading_text'] = 'Hello from template view'
        context['pets'] = Pet.objects.all()

        return context
