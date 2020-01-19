from django.shortcuts import render
from books.serializers import (BooksMobelSerializerAPI,
                               BooksMobelSerializerAPIPOST,
                               GenreSerializerAPI)
from rest_framework import views, response, permissions
from books.models import BooksModel, Genre
from django.contrib.auth.models import User


class ShowBooks(views.APIView):
    def get(self, request):
        if request.GET.get("id_book"):
            id_book = request.GET.get("id_book")
            book = BooksModel.objects.get(id=id_book)
            serializer_class = BooksMobelSerializerAPI(book)
            return response.Response(serializer_class.data)
        # else:
        #
        #     return response.Response(serializer_class.data)

        all_books = BooksModel.objects.all()
        serializer_class = BooksMobelSerializerAPI(all_books, many=True)
        return response.Response(serializer_class.data)

    def post(self, request):
        ser = BooksMobelSerializerAPIPOST(data=request.data)
        if ser.is_valid():
            ser.save()
            return response.Response({'status': "Done"})
        return response.Response({"status": "Error"})


class ShowGenre(views.APIView):
    def get(self, request):
        if request.GET.get("id_genre"):
            id_genre = request.GET.get("id_genre")
            genre = Genre.objects.get(id=id_genre)
            serializer_class = GenreSerializerAPI(genre)
            return response.Response(serializer_class.data)
        # else:
        #
        #     return response.Response(serializer_class.data)

        all_genres = Genre.objects.all()
        serializer_class = GenreSerializerAPI(all_genres, many=True)
        return response.Response(serializer_class.data)

    def post(self, request):
        ser = GenreSerializerAPI(data=request.data)
        if ser.is_valid():
            ser.save()
            return response.Response({'status': "Done"})
        return response.Response({"status": "Error"})

# Create your views here.
