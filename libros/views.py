from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libro
from .serializers import LibroSerializer

# Create your views here.
@api_view(['GET','POST'])
def libros_views(request):
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LibroSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)    
        return Response(serializer.errors, status = status.HTPP_400_BAD_REQUEST)
