from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
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


class IndexListView(ListView):
    template_name = 'cbv/index.html'
    model = Pet
    context_object_name = 'pets'
    paginate_by = 2

    def dispatch(self, request, *args, **kwargs):
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Pets list'

        return context


class IndexDetailView(DetailView):
    template_name = 'cbv/details.html'
    model = Pet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = f"{context['pet'].name} details"

        return context


class IndexCreateView(CreateView):
    fields = '__all__'
    model = Pet
    template_name = 'cbv/create_pet.html'
    success_url = reverse_lazy('cbv list')

