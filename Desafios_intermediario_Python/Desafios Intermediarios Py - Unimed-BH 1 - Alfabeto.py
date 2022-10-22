
"""
---------------------------------------
Desafios Intermediários Py - Unimed-BH
   ---------------------------------
        Desafio 1/3 - Alfabeto
   ---------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Dada a letra N do alfabeto, nos diga qual a sua posição.
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Parâmetros de entrada:
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
Parâmetros de saída:
Um único inteiro, que representa a posição da letra no alfabeto.
Dicas fornecidas pela plataforma:
FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
onde geralmente informa que tipo de informação ele está esperando receber;
FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
"""
letra = input()

letra = letra.upper()                           # Garantindo que a entrada do usuário seja uma letra maiuscula pois a lista ASCII usada abaixo para comparação é maiuscula

import string

alfabeto = list(string.ascii_uppercase)         # Definindo criação de lista com texto/string de caixa alta


print(alfabeto.index(letra)+1)                  # Vale notar que a posição da letra na lista começa em 0, logo A = 0 portanto o +1 garante a resposta na posição correta do alfabeto