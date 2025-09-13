from django.db import models

# Create your models here

class Pessoa(models.Model): 
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique= True)
    data_criacao = models.DateField(auto_now_add=True) # o parametro pega o horario atual do servidor no momento em que é criado automaticamente

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome'] # ordenar por nome A-Z

class CachorroFavorito(models.Model):
    id_raca = models.CharField(max_length=255, unique=True, help_text="ID da raça.")
    nome = models.CharField(max_length=200, help_text="nome da raça")
    descricao = models.TextField(blank= True, null= True, help_text= "Descrição da raça do cachorro.") # Blank -> pois é opcional e null -> a nível de banco de dados, caso o campo nao tenha nenhum valor
    notas = models.TextField(blank=True, null= True, help_text="Anotações pessoais do usuário.")
    criado_em = models.DateTimeField(auto_now_add=True)

    pessoa = models.ForeignKey(Pessoa, related_name='cachorros_favoritos', on_delete=models.CASCADE) #Chave estrangeira, p relação de muitos para um, Cachorro -> Pessoa || com deleçao em cascata

    def __str__(self):
        return f'{self.nome} (favorito de {self.pessoa.nome})'
    
    class Meta:
    
        ordering = ['nome']