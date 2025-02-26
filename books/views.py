from django.shortcuts import render
from django.views import generic

from . import models


class BooksListView(generic.ListView):
    model = models.Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'