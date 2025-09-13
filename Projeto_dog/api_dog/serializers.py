from rest_framework import serializers
from .models import CachorroFavorito, Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']

class CachorroFavoritoSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = CachorroFavorito

        fields = ['id', 'id_raca', 'nome', 'descricao', 'notas', 'criado_em', 'pessoa']
        read_only_fields = ['id', 'criado_em']
