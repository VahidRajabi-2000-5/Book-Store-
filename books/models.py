from django.db import models
from django.urls import reverse 

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])
        # return reverse("book_detail", kwargs={"pk": self.pk})
    