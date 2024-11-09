from django.shortcuts import render, redirect
from .models import GuestBook
from .forms import BookForm

# Create your views here.
def guest_book(request):
    books = GuestBook.objects.all()
    return render(request, "guest_book/book_list.html", {"books": books})

def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('guest_book')
    else:
        form = BookForm()
    return render(request, 'guest_book/new_book.html', {'form': form})

def book_detail(request, pk):
    book = GuestBook.objects.get(id = pk)
    return render(request, "guest_book/book_detail.html", {"book": book})

# def book_edit(request, pk):
#     book = GuestBook.objects.get(id=pk)
#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.save()
#             return redirect('guest_book')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'guest_book/edit_book.html', {'form': form})