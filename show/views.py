from django.shortcuts import render, HttpResponse
from .models import SomeData


# use /append url to fill database with this data
def append(request):
    data_entries = [
        {"book_name": "The Great Gatsby", "book_author": "F. Scott Fitzgerald", "book_pages": 180},
        {"book_name": "To Kill a Mockingbird", "book_author": "Harper Lee", "book_pages": 324},
        {"book_name": "1984", "book_author": "George Orwell", "book_pages": 328},
        {"book_name": "The Catcher in the Rye", "book_author": "J.D. Salinger", "book_pages": 224},
        {"book_name": "Pride and Prejudice", "book_author": "Jane Austen", "book_pages": 279},
        {"book_name": "The Hobbit", "book_author": "J.R.R. Tolkien", "book_pages": 310},
        {"book_name": "The Da Vinci Code", "book_author": "Dan Brown", "book_pages": 454},
        {"book_name": "The Lord of the Rings", "book_author": "J.R.R. Tolkien", "book_pages": 1178},
        {"book_name": "Harry Potter and the Sorcerer's Stone", "book_author": "J.K. Rowling", "book_pages": 309},
        {"book_name": "The Shining", "book_author": "Stephen King", "book_pages": 447},
    ]

    for entry_data in data_entries:
        SomeData.objects.create(**entry_data)

    return HttpResponse('Done!')


# on homepage url we show some of this queries
def home(request):
    object_list = SomeData.objects.filter(id__gte=1)

    return render(request, template_name='home.html', context={'data': object_list})
