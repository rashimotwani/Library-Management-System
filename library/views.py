from copy import copy
# from os import pread
from django.shortcuts import render
from . models import Book, BookCopies, IssuedBook
from django.contrib.auth.models import User
from django.contrib import messages
import math
def index(request):
    if request.method == "POST":
        id = request.POST["issueBook"]
        book = BookCopies.objects.filter(id = id)
        count = 0
        for i in book:
            if i.avail_status:
                count  = count + 1
                i.avail_status = False
                i.save()
                e = IssuedBook.objects.create(copy_id = i, email = request.user)
                e.save()
                f = Book.objects.filter(id = id)
                x = f[0].quantity
                if f[0].quantity == 1:
                    Book.objects.filter(id = id).update(avail_status = False)
                Book.objects.filter(id = id).update(quantity = x - 1)
                break
    books= Book.objects.all()
    n= len(books)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(0,nSlides), 'books': books}
    return render(request,"library/libraryLogin.html", params)

def issue(request):
    if request.method == "POST":
        id = request.POST["returnBook"]
        book = BookCopies.objects.filter(id = id)
        for i in book:
            if i.avail_status == False:
                i.avail_status = True
                i.save()
                e = IssuedBook.objects.get(copy_id = i)
                e.delete()
                f = Book.objects.filter(id = id)
                x = f[0].quantity
                Book.objects.filter(id = id).update(avail_status = True)
                Book.objects.filter(id = id).update(quantity = x + 1)
                break
    x = request.user
    IssuedBooks= IssuedBook.objects.filter( email = x )
    books = []
    for i in IssuedBooks:
        a = i.copy_id.id
        books.append(a)
    n= len(books)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(0,nSlides), 'books': books}
    return render(request,"issuedBooks/issuedBooks.html", params)


