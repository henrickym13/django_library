from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


# Create your views here.
class InflowListView(ListView):
    model = models.Inflow
    template_name= 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        book = self.request.GET.get('book')

        if book:
            queryset = queryset.filter(book__title__icontains=book)
        
        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'