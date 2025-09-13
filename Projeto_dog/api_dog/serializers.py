from rest_framework import serializers
from .models import CachorroFavorito, Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']

class CachorroFavoritoSerializer(serializers.ModelSerializer):
    pessoa = serializers.StringRelatedField(read_only=True)     #transforma o id em "pessoa: nome", em vez de pessoa: id como anteriormente.
                                                                 # pequena melhoria na exibição dos dados do JSON
    pessoa_id = serializers.PrimaryKeyRelatedField(                  # pequena melhoria na exibição dos dados do JSON
        queryset=Pessoa.objects.all(), source='pessoa', write_only=True  # recebe o id de pessoa.
    )

    class Meta:
        model = CachorroFavorito

        fields = ['id', 'id_raca', 'nome', 'descricao', 'notas', 'criado_em', 'pessoa', 'pessoa_id']
        read_only_fields = ['id', 'criado_em']
