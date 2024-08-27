from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''Representa um restaurante e suas caracteristicas.'''
    restaurantes = []
    
    def __init__(self, nome, categoria):
        '''
        Método Construtor. 
        Utilizado para chamar uma instancia(objeto).
        
        Parâmetros:
        - nome (str): recebe o nome do restaurante.
        - categoria (str): recebe a categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''
        Método STR
        Retorna uma string das caracteristicas da instancia.
        '''
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        '''
        Método de classe
        Utilizado para adicionar cada atributo de instancia em uma lista,
        e depois imprime cada um de maneira organizada.
        '''
        print(f'{'Nome do Restaurante'.ljust(25)}  {'Categoria'.ljust(25)}   {'Avaliação'.ljust(25)}   {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'|{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        '''Método que retorna um valor de acordo com a atividade do restaurante.'''
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        '''Metodo para mudar o estado do restaurante, de ativo para False ou True.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Registra uma avaliaçao para o restaurante.
        
        Parametros:
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (float): A nota que o cliente deseja dar ao restaurante.
        '''
        if 5 >= nota >= 0:  
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a media das avaliações de cada restaurante'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            else:
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho} | tipo: {item.tipo}'
                print(mensagem_sobremesa)
