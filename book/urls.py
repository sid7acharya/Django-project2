from django.urls import path
from .views import (
    #Category
    BookCategoryListView,
    BookCategoryCreateView,
    BookCategoryDeleteView,
    BookCategoryUpdateView,
    BookCategoryRetrieveView,

    # Sub-Category
    BookSubCategoryCreateview,
    BookSubCategoryDeleteview,
    BookSubCategoryListview,
    BookSubCategoryRetrieveview,
    BookSubCategoryUpdateview,

    # Author
    AuthorCreateView,
    AuthorDeleteView,
    AuthorListView,
    AuthorRetrieveView,
    AuthorUpdateView,

    # BookOption
    BookOptionCreateView,
    BookOptionDeleteView,
    BookOptionListView,
    BookOptionRetrieveView,
    BookOptionUpdateView,

    # Book
    BookCreateView,
    BookListView,
    BookRetrieveView,
    BookDeleteView,
    BookUpdateView,

    # BookRentBuy
    BookBuyRentView,
)


urlpatterns=[
    # Category
    path("categories/",BookCategoryListView.as_view(),name="categories"),
    path("category/<int:pk>/",BookCategoryRetrieveView.as_view(),name="category-retrieve"),
    path("category/<int:pk>/create/",BookCategoryCreateView.as_view(),name="category-create"),
    path("category/<int:pk>/update/",BookCategoryUpdateView.as_view(),name="category-update"),
    path("category/<int:pk>/delete/",BookCategoryDeleteView.as_view(),name="category-delete"),

    # Sub-Category
    path("subcategories/",BookSubCategoryListview.as_view(),name="subcategories"),
    path("subcategory/<int:pk>/",BookSubCategoryRetrieveview.as_view(),name="subcategory-retrieve"),
    path("subcategory/<int:pk>/create/",BookSubCategoryCreateview.as_view(),name="subcategory-create"),
    path("subcategory/<int:pk>/update/",BookSubCategoryUpdateview.as_view(),name="subcategory-update"),
    path("subcategory/<int:pk>/delete/",BookSubCategoryDeleteview.as_view(),name="subcategory-delete"),

    #Author
    path("authors/",AuthorListView.as_view(),name="authors"),
    path("author/<int:pk>/",AuthorRetrieveView.as_view(),name="author-retrieve"),
    path("author/<int:pk>/create/",AuthorCreateView.as_view(),name="author-create"),
    path("author/<int:pk>/update/",AuthorUpdateView.as_view(),name="author-update"),
    path("author/<int:pk>/delete/",AuthorDeleteView.as_view(),name="author-delete"),

    #BookOption
    path("options/",BookOptionListView.as_view(),name="book-options"),
    path("option/<int:pk>/",BookOptionRetrieveView.as_view(),name="option-retrieve"),
    path("option/<int:pk>/create/",BookOptionCreateView.as_view(),name="option-create"),
    path("option/<int:pk>/update/",BookOptionUpdateView.as_view(),name="option-update"),
    path("option/<int:pk>/delete/",BookOptionDeleteView.as_view(),name="option-delete"),


    # Book

    path("books/",BookListView.as_view(),name="books"),
    path("book/<int:pk>/",AuthorRetrieveView.as_view(),name="book-retrieve"),
    path("book/<int:pk>/create/",AuthorCreateView.as_view(),name="book-create"),
    path("book/<int:pk>/update/",AuthorUpdateView.as_view(),name="book-update"),
    path("book/<int:pk>/delete/",AuthorDeleteView.as_view(),name="book-delete"),


    path("book-buy-rent/",BookBuyRentView.as_view(),name="book-buy-rent"),


]