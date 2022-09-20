n = int(input('número: '))
divisor = 2
while divisor < n:
    print(f'{n} % {divisor} = {n % divisor}')
    if n % divisor == 0:
        break
    divisor += 1

if divisor == n:
    print('primo')
else:
    print('não é primo')
