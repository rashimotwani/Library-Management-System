from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    avail_status = models.BooleanField(default=True)
    quantity = models.IntegerField(default=10)
    book_image = models.ImageField(upload_to='library/images', default="")
    
    def __str__(self) :
        return self.book_name