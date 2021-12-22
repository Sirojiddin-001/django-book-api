from rest_framework import routers
from .views import CategoriesViewSet, SubCategoriesViewSet, BooksViewSet

router = routers.DefaultRouter()
router.register("api/categories", CategoriesViewSet, 'categories')
router.register("api/sub-categories", SubCategoriesViewSet, 'sub-categories')
router.register("api/books", BooksViewSet, 'books')

urlpatterns = router.urls
