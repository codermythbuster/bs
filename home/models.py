from django.contrib.auth.models import User
from django.db import models


# book keeping record model
class Book(models.Model):
    book_name = models.TextField(verbose_name="BOOK NAME")
    book_category = models.CharField(max_length=100, verbose_name="BOOK CATEGORY")
    book_description = models.TextField(verbose_name="BOOK DESCRIPTION")
    book_author_name = models.CharField(max_length=256, verbose_name="AUTHOR Name")
    book_price_to_sell = models.FloatField(verbose_name="Selling Price")
    username = models.ForeignKey(User,verbose_name="USERNAME",on_delete=models.CASCADE)
    book_status = models.BooleanField(default=True, verbose_name="AVAILABILITY")
    book_image = models.ImageField(verbose_name="IMAGEURL",upload_to='Uploads/book_imgs/')
    added_on = models.DateTimeField(auto_now_add=True)

    def set_username(self, request):
        self.username=request.user.username

    def __str__(self):
        return  " {} {} {} {} {}  ".format(self.book_name,self.book_author_name,self.book_category,self.book_status,self.book_image)
    

class Books_purchased (models.Model):
    user1 = models.ForeignKey(to=User,to_field=User.USERNAME_FIELD,related_name="UserSold",on_delete=models.DO_NOTHING)
    user2 = models.ForeignKey(to=User, to_field=User.USERNAME_FIELD,related_name="UserPurchased", on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(to = Book,on_delete=models.CASCADE , to_field="id" ,)

    def __str__(self):
        return "{} {} {} {}".format(self.trans_id,self.book_id,self.user1,self.user2)


   

