lista_faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(lista_faturamento.values())

for estado, valor in lista_faturamento.items():
    participacao = (valor/total)*100
    print(f'A participação de {estado} foi de {participacao:.2f}%')