from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from app import metrics
from author.models import Author
from publishing.models import Publishing
from supplier.models import Supplier


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        isbn_10 = self.request.GET.get('isbn_10')
        isbn_13 = self.request.GET.get('isbn_13')
        author = self.request.GET.get('author')
        publishing = self.request.GET.get('publishing')
        supplier = self.request.GET.get('supplier')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if isbn_10:
            queryset = queryset.filter(isbn_10__icontains=isbn_10)
        if isbn_13:
            queryset = queryset.filter(isbn_13__icontains=isbn_13)
        if author:
            queryset = queryset.filter(author__id=author)
        if publishing:
            queryset = queryset.filter(publishing__id=publishing)
        if supplier:
            queryset = queryset.filter(supplier__id=supplier)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_metrics'] = metrics.get_book_metrics()
        context['authors'] = Author.objects.all()
        context['publishies'] = Publishing.objects.all()
        context['suppliers'] = Supplier.objects.all()
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    template_name = 'book_create.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('book_list')


class BookDetailView(LoginRequiredMixin, DetailView):
    model = models.Book
    template_name = 'book_detail.html'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('book_list')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')