from django.shortcuts import render
import requests
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CachorroFavorito, Pessoa
from .serializers import CachorroFavoritoSerializer, PessoaSerializer

# Create your views here.

api_url = "https://dogapi.dog/api/v2/breeds"

class DogApiBreedsView(APIView): # para pegar os dados da api externa 
    def get(self, request, *args, **kwargs):  #argumentos posicionais e nomeados 
        try: 
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            return Response(data.get('data', []))
        except requests.exceptions.RequestException as e:
            return Response( {"error": f"erro ao contatar a DOG API. {e}" }, status= status.HTTP_503_SERVICE_UNAVAILABLE)
        
class PessoaViewSet(viewsets.ModelViewSet):
    # endpoint para criar, ler, atualizar e deletar pessoas.

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class CachorroFavoritoViewSet(viewsets.ModelViewSet):
    # endpoint para criar ler, atualizar e deletar cachorros.

    queryset = CachorroFavorito.objects.all()
    serializer_class = CachorroFavoritoSerializer