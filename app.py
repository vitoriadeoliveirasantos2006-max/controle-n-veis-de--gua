
from colorama import Fore, Style

# LISTA COM AS SITUACOES DO RESERVATORIO
situacoes = [
    "Muito baixo (critico)",
    "Baixo",
    "Medio",
    "Alto",
    "Muito alto (alerta)"
]

# FUNCAO PARA DEFINIR A COR DO ALERTA
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# ENTRADA DE DADOS
capacidade = float(input("Informe a capacidade total do reservatorio em litros: "))
quantidade_atual = float(input("Informe a quantidade atual de agua em litros: "))

# CALCULO DO NIVEL DE AGUA
if capacidade <= 0:
    print("A capacidade deve ser maior que zero.")

elif quantidade_atual < 0 or quantidade_atual > capacidade:
    print("Quantidade invalida! Verifique os valores informados.")

else:
    porcentagem = (quantidade_atual / capacidade) * 100

    # IDENTIFICACAO DO NIVEL
    if porcentagem <= 20:
        nivel = 1
    elif porcentagem <= 40:
        nivel = 2
    elif porcentagem <= 60:
        nivel = 3
    elif porcentagem <= 80:
        nivel = 4
    else:
        nivel = 5

    # EXIBICAO DO RESULTADO
    cor = definir_cor(nivel)
    mensagem = situacoes[nivel - 1]

    print()
    print(cor + "Nivel do reservatorio:", nivel)
    print("Quantidade de agua:", quantidade_atual, "litros")
    print("Reservatorio preenchido:", round(porcentagem, 2), "%")
    print("Situacao:", mensagem + Style.RESET_ALL)