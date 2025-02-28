from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models


class BooksListView(generic.ListView):
    model = models.Book
    template_name = "books/books_list.html"
    context_object_name = "books"

    def get_queryset(self):
        return models.Book.objects.all().order_by(
            "-datetime_created", "-datetime_modified"
        )


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(generic.CreateView):
    model = models.Book
    fields = [
        "title",
        "author",
        "content",
        "price",
        "cover",
    ]
    template_name = "books/book_create.html"
    # success_url = reverse_lazy('books_list')


class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = [
        "title",
        "author",
        "content",
        "price",
        "cover",
    ]
    template_name = "books/book_update.html"


class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = "books/book_delete.html"
    context_object_name = "book"
    success_url = reverse_lazy("books_list")
