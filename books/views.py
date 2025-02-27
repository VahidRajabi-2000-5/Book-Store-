from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models


class BooksListView(generic.ListView):
    model = models.Book
    template_name = "books/books_list.html"
    context_object_name = "books"
    
    def get_queryset(self):
        return models.Book.objects.all().order_by('-datetime_created')
    


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(generic.CreateView):
    model = models.Book
    fields = ["title", "author", "content", "price",]
    template_name = "books/book_create.html"
    context_object_name = "book_form"
    # success_url = reverse_lazy('books_list')
