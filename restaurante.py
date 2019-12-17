"""
Crie um progrma que verifica o nome informado pelo usuário e se consta na lista; 
EX: Checar se possui reserva em um restaurante. 
"""


print('***** CANTINA DA MÃE JOANA *****\n')


lista_convidados = ['arthur', 'maria', 'roberto', 'naime', 'letícia', 'leidimara']

cardapio = ['lasanha', 'hamburguer', 'fritas', 'picanha', 'feijoada', 'bisteca']

nome = input('Boa noite SR(a), informe seu nome: ').lower()



if nome in lista_convidados:
    print(f'Seja bem-vindo {nome.title()}, entre e faça seu pedido.\n ')


else:
    print(f'Desculpe {nome.title()}, seu nome não está na lista.\n'
        f'Obrigado pela a preferência, VOLTE SEMPRE!\n')
    quit()



# Cliente pode escolher o prato desejado.

print("********** C A R D Á P I O **********\n")

for menu in cardapio:
    print(f'{menu.title()}: ')

print("\n" + "*" * 37)

pedido_menu = input('\nDigite o prato desejado: ').lower()

if pedido_menu in cardapio:
    print(f'Ótima escolha, a {pedido_menu.title()} está deliciosa!')
   
   
else:
    print(f'Desculpe, não estamos servindo {pedido_menu.title()} hoje.\n'
          f'OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE!')
    quit()

print("\nOBRIGADO E VOLTE SEMPRE!")
