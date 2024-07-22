from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


# Create your views here.
class BookListView(ListView):
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
            queryset = queryset.filter(author__icontains=author)
        if publishing:
            queryset = queryset.filter(publishing__icontains=publishing)
        if supplier:
            queryset = queryset.filter(supplier__icontains=supplier)
        
        return queryset


class BookCreateView(CreateView):
    model = models.Book
    template_name = 'book_create.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('book_list')


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'book_detail.html'


class BookUpdateView(UpdateView):
    model = models.Book
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = models.Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')