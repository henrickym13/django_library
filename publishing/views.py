from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


# Create your views here.
class PublishingListView(ListView):
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


class PublishingCreateView(CreateView):
    model = models.Publishing
    template_name = 'publishing_create.html'
    form_class = forms.PublishingForm
    success_url = reverse_lazy('publishing_list')


class PublishingDetailView(DetailView):
    model = models.Publishing
    template_name = 'publishing_detail.html'


class PublishingUpdateView(UpdateView):
    model = models.Publishing
    template_name = 'publishing_update.html'
    form_class = forms.PublishingForm
    success_url = reverse_lazy('publishing_list')


class PublishingDeleteView(DeleteView):
    model = models.Publishing
    template_name = 'publishing_delete.html'
    success_url = reverse_lazy('publishing_list')