from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import models, forms


# Create your views here.
class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        book = self.request.GET.get('book')

        if book:
            queryset = queryset.filter(boook__title__icontains=book)
        
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['book_metrics'] = metrics.get_book_metrics()
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context


class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'