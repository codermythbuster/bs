from django.contrib import admin

from .models import Book, Books_purchased


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Books_purchased)
class BookPurchasedAdmin(admin.ModelAdmin):
    pass
