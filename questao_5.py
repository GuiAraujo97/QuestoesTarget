string = input('Digite a string que deseja inverter: ')
string_new = ''
i = 0
for letra in string:
    string_new += string[len(string)-1-i]
    i += 1
print(f'Sua string invertida é: \n{string_new}')