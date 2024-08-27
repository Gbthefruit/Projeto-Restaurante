from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_macarrao = Prato('Macarrão a Bolonhesa', 8.00, 'Macarrão com carne moída')
prato_macarrao.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete de Baunilha', 10.00, 'Gelada', 'médio')
sobremesa_sorvete.aplicar_desconto()
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_macarrao)
restaurante_praca.adicionar_cardapio(sobremesa_sorvete)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
