from django.db import models
from django.contrib.auth.models import User

# book keeping record model
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.TextField()
    book_category = models.CharField(max_length=100)
    book_description = models.TextField()
    book_author_name = models.CharField(max_length=256)
    book_price_to_sell = models.FloatField()
    username = models.ForeignKey(User)

    def __str__(self):
        string = f"{self.book_id se}"





