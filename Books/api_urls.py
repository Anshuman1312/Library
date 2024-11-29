from django.urls import path
from .views import *

urlpatterns = [
    path('libraries/', LibraryAPIView.as_view(), name='library-list'),
    path('UpdateDeleteAndGetSpecificLibrary/<int:id>', UpdateDeleteAndGetSpecificLibrary.as_view(), name='Update-Delete-Get-Specific-Library'),
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('UpdateDeleteAndGetSpecificBook/<int:id>', UpdateDeleteAndGetSpecificBook.as_view(), name='Update-Delete-Get-Specific-Book'),
]
