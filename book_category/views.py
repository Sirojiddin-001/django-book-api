from rest_framework import viewsets, permissions
from .models import Categories, SubCategories, Books
from .serializers import CategorySerializer, SubCategorySerializer, BookSerializer


# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class SubCategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = SubCategories.objects.all()
    serializer_class = SubCategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
