from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Links
from .forms import LinkForm


def HomePage(request):
    return render(request, 'main/home.html')


def AboutPage(request):
    return render(request, 'main/about.html')


class LinksPage(ListView):
    model = Links
    template_name = 'main/short_links.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LinksPage, self).get_context_data(**kwargs)
        form = LinkForm(initial={'user': self.request.user})

        ctx['form'] = form
        ctx['links'] = Links.objects.filter(user=self.request.user).order_by('-id')
        return ctx

    def post(self, request, *args, **kwargs):
        form = LinkForm(request.POST)
        if form.is_valid():
            links = form.save()
            links.save()

        return redirect(request.path)