from django.contrib import admin

# Register your models here.
from .models import Book, BookCopies, IssuedBook
admin.site.register(Book)

admin.site.register(BookCopies)
admin.site.register(IssuedBook)
