""" 32) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram 
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""

cod_cidade = []
num_veiculos = []
num_acidentes = []

def resultados():
    minimo = min(num_acidentes)
    resultado = (num_acidentes.index(minimo))
    print("O código",resultado,"apresenta a menor numero de acidentes de transito uqe é de",minimo)

    soma = sum(num_veiculos)
    qtd = len(num_veiculos)
    resultado2 = (soma/qtd)
    print("A média de veículos ans cinco cidades é de",resultado2)

    print("")

    

def dados():

    for i in range(2):
        cidade = int(input("Digite o código da cidade: "))
        cod_cidade.append(cidade)
        veiculos = int(input("Digite o número de veículos: "))
        num_veiculos.append(veiculos)
        acidentes = int(input("Digite o número de acidenstes: "))
        num_acidentes.append(acidentes)
    resultados()


def main():
    while True:
        menu = int(input("Como deseja proseguir: \n1-Informar dados \n2-Sair "))

        if(menu == 1):
            dados()
        if(menu == 2):
            break

main()