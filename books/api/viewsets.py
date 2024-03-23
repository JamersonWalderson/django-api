from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from books.api import serializers
from books import models
from rest_framework.permissions import IsAuthenticated

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Livro cadastrado com sucesso",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "status": "error",
                    "message" "Erro ao cadastrar" "data": serializer.error,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
