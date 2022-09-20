## Funções ##
def pede_idade(mensagem):
    """Função que pede a idade do usuário

    outras informações...
    ...
    """
    idade = int(input(mensagem))
    return idade



## Código Principal ##

idade = pede_idade('Digite sua idade:  ' )

if idade > 18:
    print('você tem mais de 18 anos')
else:
    print('você tem menos de 18 anos')

print('fim')

