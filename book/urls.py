from django.urls import path

from book.views import BookCreateView, BookDetailsView, BookView, CategoryCreateView, CategoryView, PublisherCreateView, PublisherDetailsView, CategoryDetails, PublisherView, AuthorView, AuthorDetailsview, AuthorCreateView

urlpatterns = [
    path("book/", BookView.as_view(), name="book-all"),
    path("book/create", BookCreateView.as_view(), name="create-book"),
    path("book/<uuid:id>", BookDetailsView.as_view(), name="book-details"),
    
    path("category", CategoryView.as_view(), name="category-all"),
    path("category/create", CategoryCreateView.as_view(), name="category-create"),
    path("category/<uuid:id>", CategoryDetails.as_view(), name="category-details"),
    
    path("publisher/", PublisherView.as_view(), name="publisher-view"),
    path("publisher/create", PublisherCreateView.as_view(), name="publisher-create"),
    path("publisher/<uuid:id>", PublisherDetailsView.as_view(), name="publisher-details"),
    
    path('author/', AuthorView.as_view(), name="author-all"),
    path('author/create', AuthorCreateView.as_view(), name="create-author"),
    path('author/<uuid:id>', AuthorDetailsview.as_view(), name="author-details")
]