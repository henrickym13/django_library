from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


# Create your views here.
class PublishingListView(LoginRequiredMixin, ListView):
    model = models.Publishing
    template_name = 'publishing_list.html'
    context_object_name = 'publishers'
    paginate_by= 10

    def get_queryset(self):
        queryset =  super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset


class PublishingCreateView(LoginRequiredMixin, CreateView):
    model = models.Publishing
    template_name = 'publishing_create.html'
    form_class = forms.PublishingForm
    success_url = reverse_lazy('publishing_list')


class PublishingDetailView(LoginRequiredMixin, DetailView):
    model = models.Publishing
    template_name = 'publishing_detail.html'


class PublishingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Publishing
    template_name = 'publishing_update.html'
    form_class = forms.PublishingForm
    success_url = reverse_lazy('publishing_list')


class PublishingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Publishing
    template_name = 'publishing_delete.html'
    success_url = reverse_lazy('publishing_list')