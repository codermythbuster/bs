from rest_framework import serializers

from .models import Book


class BookSearializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
