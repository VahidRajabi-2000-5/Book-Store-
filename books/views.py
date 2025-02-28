from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


class BooksListView(generic.ListView):
    model = models.Book
    template_name = "books/books_list.html"
    context_object_name = "books"
    paginate_by = 4

    def get_queryset(self):
        return models.Book.objects.all().order_by(
            "-datetime_created", "-datetime_modified"
        )


# class BookDetailView(generic.DetailView):
#     model = models.Book
#     template_name = "books/book_detail.html"
#     context_object_name = "book"

@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(models.Book, pk=pk)

    comments = book.comments.all()

    if request.method == "POST":
        comment_form = forms.CommentForm(request.POST)
        
        if comment_form.is_valid(): 
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = forms.CommentForm()
    else:
        comment_form = forms.CommentForm()

    return render(
        request,
        "books/book_detail.html",
        {
            "book": book,
            "comments": comments,
            "comment_form": comment_form,
        },
    )


class BookCreateView(LoginRequiredMixin, generic.CreateView):
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


class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = models.Book
    fields = [
        "title",
        "author",
        "content",
        "price",
        "cover",
    ]
    template_name = "books/book_update.html"
    
    def test_func(self):
        book = self.get_object()
        return book.user == self.request.user 


class BookDeleteView(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
    model = models.Book
    template_name = "books/book_delete.html"
    context_object_name = "book"
    success_url = reverse_lazy("books_list")
    
    def test_func(self):
        book = self.get_object()
        return book.user == self.request.user
