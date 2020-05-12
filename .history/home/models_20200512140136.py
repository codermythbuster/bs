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
    username = models.ForeignKey(User,verbose_name="USERNAME",on_delete=models.CASCADE)
    book_status = models.BooleanField(default=False, verbose_name="AVAILABILITY")
    book_image = models.ImageField(verbose_name="IMAGE URL")
    def __str__(self):
        return  " {} {} {} {} {} {} ".format(self.book_id,self.book_name,self.book_author_name,self.book_category,self.book_status,self.book_image)
    

class Books_purchased (models.Model):
    trans_id = models.AutoField(verbose_name="Transaction ID",primary_key=True)
    user1 = models.ForeignKey(to=User,to_field=User.USERNAME_FIELD,verbose_name="User Sold",on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(to=User, to_field=User.USERNAME_FIELD,verbose_name="User Purchased", on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(Book,models.DO_NOTHING)

    def __str__(self):
        return "{} {} {} {}".format(self.trans_id,self.book_id,self.user1,self.user2)

   





