from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import (
    FavoriteCreateDestroyView,
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet,
    SubscribeCreateDestroyView,
    SubscribeListView
)

router = DefaultRouter()

router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('tags', TagViewSet, basename='tags')

urlpatterns = [
    path('recipes/<int:id>/favorite/',
         FavoriteCreateDestroyView.as_view(),
         name='favorite'),
    path('users/<int:id>/subscribe/',
         SubscribeCreateDestroyView.as_view(),
         name='subscribe'),
    path('users/subscriptions/',
         SubscribeListView.as_view(),
         name='subscriptions'),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
