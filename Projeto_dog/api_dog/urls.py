from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, CachorroFavoritoViewSet, DogApiBreedsView

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet) 
router.register(r'favoritos', CachorroFavoritoViewSet) 

urlpatterns = [
    path('raca/', DogApiBreedsView.as_view()), 
    path('', include(router.urls)),
]