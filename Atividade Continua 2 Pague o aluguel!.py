Divida = int(input('Digite o valor da dívida: '))
Mensalidade = int(input('Digite o valor do pagamento: '))
pagamento = 0

while Divida != 0 <= Divida:
    print ('pagamento:',pagamento + 1)
    print ('antes =',Divida)
    pagamento = pagamento + 1
    Divida = Divida - Mensalidade
    if Divida >= 0:
        print ('depois =',Divida)
        print ('-----')

    else:
        print ('depois = 0')
        print ('-----')
