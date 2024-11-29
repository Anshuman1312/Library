from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated

class LibraryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            libraries = Library.objects.all()
            serializer = LibrarySerializer(libraries, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})

    def post(self, request):
        try:
            serializer = LibrarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
    
class UpdateDeleteAndGetSpecificLibrary(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id=None):
        try:
            library=Library.objects.get(id=id)
            serializer = LibrarySerializer(library,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
    
    def delete(self,request,id=None):
        try:
            library=Library.objects.get(id=id)
            if library:
                library.delete()
                return Response("Deleted")
            else:
                return Response("Not Found")
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
        
    def get(self,request,id=None):
        try:
            library=Library.objects.get(id=id)
            serializer = LibrarySerializer(library)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})

class BookAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})

    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
        
class UpdateDeleteAndGetSpecificBook(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id=None):
        try:
            library=Book.objects.get(id=id)
            serializer = BookSerializer(library,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
    
    def delete(self,request,id=None):
        try:
            library=Book.objects.get(id=id)
            if library:
                library.delete()
                return Response("Deleted")
            else:
                return Response("Not Found")
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
        
    def get(self,request,id=None):
        try:
            library=Book.objects.get(id=id)
            serializer = BookSerializer(library)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Something went wrong" : str(e)})
