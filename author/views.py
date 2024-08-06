from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


# Create your views here.
class AuthorListView(LoginRequiredMixin, ListView):
    model = models.Author
    template_name = 'author_list.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = models.Author
    template_name = 'author_create.html'
    form_class = forms.AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = models.Author
    template_name = 'author_detail.html'


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Author
    template_name = 'author_update.html'
    form_class = forms.AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')