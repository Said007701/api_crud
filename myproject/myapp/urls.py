from django.urls import path
from . import views 
from .views import BookListView, BookDetailView 

urlpatterns = [
    path('', views.index, name='index'),  
    path('list/', views.list_book, name='list_book'),
    path('create/', views.Create, name='Create'),  
    path('update/<int:list_id>/', views.update_book, name='update_book'),  
    path('delete/<int:list_id>/', views.delete_book, name='delete_book'),  
    path('api/book/', BookListView.as_view(), name='book-list'),  
    path('api/book/<int:pk>/', BookDetailView.as_view(), name='book-detail')
]
