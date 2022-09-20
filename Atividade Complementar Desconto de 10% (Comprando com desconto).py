Valor = float(input('Digite o valor: '))
Qtd = int(input('Digite a quantidade: '))
Dt = Qtd + 10
Total = Valor * Qtd
Desconto = Total * Dt / 100
vf = Total - Desconto
print(f'{Total:.2f}')
print(f'{vf:.2f}')
