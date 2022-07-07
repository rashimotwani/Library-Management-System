from django.shortcuts import render
from . models import Book
import math
def index(request):
    books= Book.objects.all()
    n= len(books)
    nSlides= n//4 + math.ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'books': books}
    return render(request,"library/libraryLogin.html", params)
