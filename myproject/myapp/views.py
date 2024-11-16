from django.shortcuts import render,redirect
from .models import Gile
from .forms import GileForm

def Create(request):
    if request.method == "POST":
        form = GileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = GileForm()

    return render(request, 'create.html',{'form':form})

def list_book(request):
    books = Gile.objects.all()
    return render(request,'list.html', {'books':books})

def update_book(request, list_id):
    book = Gile.objects.get(id=list_id)
    if request.method == 'POST':
        form = GileForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = GileForm(instance=book)
    
    return render(request, 'update.html', {'form': form, 'book': book})

def delete_book(request, list_id):
    book = Gile.objects.get(id=list_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_book')
    
    return render(request, 'delete.html', {'book': book})


def index(request):
    return render(request,'list.html')

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gile
from .serializers import GileSerializers

class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Gile.objects.get(pk=pk) 
        except Gile.DoesNotExist:
            return Response({"error": "Книга не найдена"}, status=404)

        serializer = GileSerializers(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            book = Gile.objects.get(pk=pk)
        except Gile.DoesNotExist:
            return Response({"error": "Книга не найдена"}, status=404)

        
        serializer = GileSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            book = Gile.objects.get(pk=pk)
        except Gile.DoesNotExist:
            return Response({"error": "Книга не найдена"}, status=404)

        book.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
class BookListView(APIView):
    def get(self, request):
        books = Gile.objects.all()
        serializer = GileSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)