from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'review']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タイトルを入力'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '著者名を入力'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': '感想を入力（任意）'}),
        }