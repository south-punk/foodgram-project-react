from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import (
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet
)


router = DefaultRouter()

router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
