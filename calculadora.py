# Criar um programa que realize a equação que o usuário fornecer. 

print('#CALCULADORA#\n')

        

while True:
    pergunta = input("Qual operação (+, -, *, /) você quer fazer ou 'q' para sair: ")
    if pergunta == 'q' or pergunta == 'Q':        
        break
    
    elif pergunta == '+' or pergunta == '-' or pergunta == '*' or pergunta == '/':
        
        valor1 = int(input('\nDigite o primeiro valor: '))     
                
        valor2 = int(input('Digite o segundo valor: '))
                             
              
    else:
        print('\nOperação inválida!\n')     
        

    if pergunta == '+':
        print(f'\nO resultado é {valor1 + valor2}!\n')

    elif pergunta == '-':
        print(f'\nO resultado é {valor1 - valor2}!\n')

    elif pergunta == '*':
        print(f'\nO resultado é {valor1 * valor2}!\n')

    elif pergunta == '/':
        print(f'\nO resultado é {valor1 / valor2}\n')

        




