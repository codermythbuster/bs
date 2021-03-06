from django.db import models
from django.contrib.auth.models import User

# book keeping record model
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True,verbose_name="BOOK ID")
    book_name = models.TextField(verbose_name="BOOK NAME")
    book_category = models.CharField(max_length=100,verbose_name="BOOK CATEGORY")
    book_description = models.TextField(verbose_name="BOOK DESCRIPTION")
    book_author_name = models.CharField(max_length=256, verbose_name="AUTHOR Name")
    book_price_to_sell = models.FloatField(verbose_name="Selling Price")
    username = models.ForeignKey(User,verbose_name="USERNAME")
    book_status = models.BooleanField(default=False, verbose_name="AVAILABILITY")
    book_image = models.ImageField(verbose_name="IMAGE URL")
    def __str__(self):
        return  " {} {} {} {} {} {} ".format(self.book_id,self.book_name,self.book_author_name,self.book_category,self.book_status,self.book_image)
    

class Books_purchsed (models.Model):
    trans_id = models.IntegerField(verbose_name="Transaction ID")
   





