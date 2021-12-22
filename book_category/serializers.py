from rest_framework import serializers
from .models import Categories, SubCategories, Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
