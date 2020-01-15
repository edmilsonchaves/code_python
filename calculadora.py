# Criar um programa que realize a equação que o usuário fornecer. 


print("*" * 5 +" C A L C U L A D O R A " + "*" * 5)

valor1 = int(input('\nDigite o primeiro valor: '))

valor2 = int(input('Digite o segundo valor: '))

equacao = ('(+) Soma', '(-) Subtração', '(*) Multiplicação', '(/) Divisão')

print("\nESCOLHA O SINAL DA EQUAÇÃO QUE DESEJA REALIZAR\n ")

for e in equacao:
    print(e)

choice = input('\nDigite o sinal da equação que deseja realizar: ')

if choice == '+':
    print(f'O Resultado é {valor1 + valor2}')

elif choice == '-':
    print(f'O Resultado é {valor1 - valor2}')

elif choice == '*':
    print(f'O Resultado é {valor1 * valor2}')

elif choice == '/':
    print(f'O Resultado é {valor1 / valor2}')

else:
    print(f'Você digitou {choice}, não é um sinal de equação!')



