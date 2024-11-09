from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_book, name="guest_book"),
    path("post/", views.new_book, name = "new_book"),
    path("<int:pk>", views.book_detail, name = "book_detail"),
    # path("<int:pk>/edit", views.book_edit, name = "book_edit")
]