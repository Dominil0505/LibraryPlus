from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework import generics

from rest_framework import permissions
from book.models import Author, Book, Category, Publisher

from book.serializers import AuthorSerializer, BookSerializer, CategorySerializer, PublisherSerializer

class BookView(generics.ListAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookCreateView(generics.CreateAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryView(generics.ListAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryCreateView(generics.CreateAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

class PublisherView(generics.ListAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAdminUser]

class PublisherCreateView(generics.CreateAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAdminUser]

class PublisherDetailsView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'
    
class AuthorView(generics.ListAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]

class AuthorCreateView(generics.CreateAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]

class AuthorDetailsview(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [CamelCaseJSONParser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'