from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime
# from django.conf import settings

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField
    id = models.AutoField(auto_created=True, primary_key=True)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    avail_status = models.BooleanField(default=True)
    quantity = models.IntegerField(default=10)
    book_image = models.ImageField(upload_to='library/images', default="")
    
    def __str__(self) :
        return self.book_name

class BookCopies(models.Model):
    copy_id = models.AutoField(auto_created=True, primary_key=True)
    id = models.ForeignKey("Book", on_delete=models.CASCADE)
    avail_status = models.BooleanField(default=True)


class IssuedBook(models.Model):
    copy_id = models.ForeignKey(BookCopies, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField(default=datetime.datetime.now)
