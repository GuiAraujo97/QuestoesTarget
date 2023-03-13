numero = int(input('Digite um número que deseja encontrar na sequência de Fibonacci: '))
fibo_list = [0,1]

while fibo_list[-1] < numero:
    soma = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(soma)

if numero in fibo_list:
    print(f'{numero} faz parte da sequência de Fibonacci')
else: 
    print(f'{numero} NÃO FAZ PARTE da sequência de Fibonacci')