from django import forms
from .models import GuestBook

class BookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ("description", "writer")