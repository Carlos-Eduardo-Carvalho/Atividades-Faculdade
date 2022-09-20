Ano_c = int(input('Digite o ano de inicio: ', True))
Ano_f = int(input('Digite o ano final: ', True))
Ano_b = 0

while Ano_c < Ano_f + 1:
    if Ano_c % 4 == 0 and Ano_c % 100 == 0 and Ano_c < 400:
        Ano_c = Ano_c + 1
    if Ano_c % 400 != 0 and Ano_c % 100 == 0:
        Ano_c = Ano_c + 1
    else:
        pass
    if Ano_c % 4 == 0:
        Ano_b = Ano_b + 1
        print (Ano_c)
        Ano_c = Ano_c + 1
    else:
        if Ano_c % 4 == 0:
            Ano_b = Ano_b + 1
            print (Ano_c)
            Ano_c = Ano_c + 1
        else:
            Ano_c = Ano_c + 1
if Ano_c > Ano_f:
    print (f'bissextos: {Ano_b}')
