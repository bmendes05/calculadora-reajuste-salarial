
try:
    salario = float(input('qual o valor do salario do funcionario?'))
    porcentagem = float(input('qual a porcentagem de aumento?'))
    aumento = salario * (porcentagem / 100)
    novo_salario = salario + aumento

    print(f'\nSalário atual: R$ {salario:.2f}')
    print(f'Valor do aumento: R$ {aumento:.2f}')
    print(f'Novo salário: R$ {novo_salario:.2f}')

except ValueError:
    print('Por favor, insira um valor numérico válido para o salário e a porcentagem de aumento.')

input('Pressione Enter para sair...')

