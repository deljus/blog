from django.views import View
from django.shortcuts import render


class IndexView(View):
    template_name = 'pages/index.html'

    def get(self, request):
        return render(request, self.template_name)
