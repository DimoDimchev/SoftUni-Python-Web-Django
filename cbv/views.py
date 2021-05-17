from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        return render(request, 'cbv/index.html')

    def post(self, request):
        pass
