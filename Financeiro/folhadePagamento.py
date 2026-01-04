# FOLHA DE PAGAMENTO
from os import system, name
# Definindo o sistema operacional que está rodando! posix - linux e mac e nt - windows
system('cls') if (name == 'nt') else system('clear')

def calculcar_inss(salario):
    """ 
    Calcular o valor do INSS com base no salário bruto.
    """
    if salario > 8537.55:
        return  900.70
    if salario >  5055.01:
        return salario * 0.14
    elif salario > 3033.01:
        return salario * 0.12
    elif salario > 1621.00:
        return salario * 0.09
    else:
        return salario * 0.075


# Calculo do IR
def calcular_ir(base):
    """
    Calcula o imposto de renda com base no salário base.
    Retorna a alíquota e o valor do imposto.
    """

    if base > 4664.68:
        return 0.275, (base * 0.275) -  869.36
    elif base > 3751.06:
        return 0.225, (base * 0.225) - 636.13
    elif base > 2826.66:
        return 0.15, (base * 0.15) - 354.80
    elif base > 2428.61:
        return 0.075, (base * 0.075) - 142.80
    else:
        return 0, 0


print('*** FOLHA DE PAGAMENTO ***')

salario = float(input('Informe o seu salário: R$'))

# Calculos
inss = calculcar_inss(salario)
base = salario - inss
irP, ir = calcular_ir(base)
salario_liquido = base - ir

print(f"""
Salário bruto:         R${salario:.2f}
Salário base:          R${base:.2f}
INSS:                  R${inss:.2f}
IR: ({irP*100:.1f}%)   R${ir:.2f}
Valor IR:              R${ir:.2f} 
Salário Liquido:       R${salario_liquido:.2f}
""")
