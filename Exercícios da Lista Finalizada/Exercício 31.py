""" 31) Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador 
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo. """

import random
numero_maquina = random.randint(1, 10)

print("Jogo de Par ou Ímpar")

qtd_vitoria = []

def main():
    while True:

        aposta = int(input("Escolha seu time: \n1-Par \n2-Ímpar "))

        if(aposta == 1 ):
            print("Você escolheu Par")
        if(aposta == 2):
            print("Você escolheu Ímpar")

        numero_jogador = int(input("Digite um número inteiro entre 1 e 10: "))
        if(numero_jogador > 10) or (numero_jogador < 0):
            print("Número Inválido")
            main()

        else:
            soma = (numero_maquina + numero_jogador)
            resultado = (soma % 2)

            if(resultado == 0) and (aposta == 1):
                print("Você Venceu")
                print("Resultado do Jogo:",soma)
                qtd_vitoria.append(aposta)


                escolha = str(input("Deseja jogar novamente (S/N): "))
                if(escolha == "N"):
                    print("Você venceu",len(qtd_vitoria),"vez(es) consecutiva(s)")
                    break
                if(escolha == "S"):
                    main()

            else:
                print("A Máquina Venceu")
                print("Resultado do Jogo:",soma)
                print("Você venceu",len(qtd_vitoria),"vez(es) consecutiva(s)")
                break
        break
main()
