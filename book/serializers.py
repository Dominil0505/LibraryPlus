from rest_framework import serializers

from book.models import Author, Book, Category, Publisher

class BookSerializer(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(
        queryset = Author.objects.all(),
        slug_field = 'name'
    )
    
    publisher = serializers.SlugRelatedField(
        queryset = Publisher.objects.all(),
        slug_field = 'name'
    )
    
    categories = serializers.SlugRelatedField(
        many = True,
        queryset = Category.objects.all(),
        slug_field = 'name'
    )
    
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']