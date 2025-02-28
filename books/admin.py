from django.contrib import admin

from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "price",
    ]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "book",
        "datetime_created",
        "text",
    ]
    list_editable = ['text']

