from copy import copy
from django.shortcuts import render
from . models import Book, BookCopies, IssuedBook
import math
def index(request):
    if request.method == "POST":
        id = request.POST["issueBook"]
        book = BookCopies.objects.filter(id = id)
        print(request.user)
        for i in book:
            if i.avail_status:
                i.avail_status = False
                i.save()
                e = IssuedBook.objects.create(copy_id = i, username = request.user)
                e.save()
                break
        
    books= Book.objects.all()
    n= len(books)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(0,nSlides), 'books': books}
    return render(request,"library/libraryLogin.html", params)

def issue(request):
    # if request.method == "POST":
    #     id = request.POST["issueBook"]
    #     book = BookCopies.objects.filter(id = id)
    #     print(request.user)
    #     for i in book:
    #         if i.avail_status:
    #             i.avail_status = False
    #             i.save()
    #             e = IssuedBook.objects.create(copy_id = i, username = request.user)
    #             e.save()
    #             break
        
    books= IssuedBook.objects.all()
    n= len(books)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(0,nSlides), 'books': books}
    return render(request,"library/issuedBooks.html", params)


