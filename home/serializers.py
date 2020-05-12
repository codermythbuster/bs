from rest_framework import serializers

from .models import Book


class BookSearializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_name', 'book_author_name', 'book_category', 'book_description', 'book_author_name',
                  'book_price_to_sell', 'username', 'book_status', 'book_image']
