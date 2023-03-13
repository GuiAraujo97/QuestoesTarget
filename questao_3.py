import json

with open('dados.json') as arquivo:
    dados = json.load(arquivo)

valor_max = 0
valor_total = 0
dias_totais = 0
dias_que_superou = 0

lista = []

for dia in dados: 
    if dia['valor'] != 0:
        lista.append(dia)

for dia in lista:
    if dia['valor'] > valor_max:
        valor_max = dia['valor']
        dia_vmax = dia['dia']
        valor_min = valor_max

for dia in lista:
    if dia['valor'] < valor_min:
        valor_min = dia['valor']
        dia_vmin = dia['dia']

for dia in lista:
    valor_total += dia['valor']

for dia in lista:
    dias_totais += 1

media_mensal = valor_total/dias_totais

for dia in lista:
    if dia['valor'] > media_mensal:
        dias_que_superou += 1

print(f'O menor valor de faturamento foi R${valor_min:.2f} e ocorreu no dia {dia_vmin} do mês.')
print(f'O maior valor de faturamento foi R${valor_max:.2f} e ocorreu no dia {dia_vmax} do mês.')
print(f'O valor de faturamento diário superou à média mensal em: {dias_que_superou} dias nesse mês.')