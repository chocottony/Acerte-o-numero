import random
from colorama import Fore, Back, Style

jogarNovamente = "sim"
print("Bem vindo ao Acerte o Número!\nNeste jogo você possui três tentativas de acertar um número que vai de 0 a 10.\nVamos começar!\n")

while (jogarNovamente == "Sim" or jogarNovamente == "sim"):
    while True:
        num_r = random.randrange(0, 10)
        numero = int(input("Primeira tentativa\nQual o número: "))

        if numero < 0 or numero > 10:
            print("Você digitou um número inválido, tente de novo.\n")
            numero = int(input("Qual o número: "))
        if numero == num_r:
            print("Parabéns você acertou o número de primeira, que sorte hein!\Te vejo na próxima")
            break
        elif numero != num_r:
            print("Infelizmente não foi dessa vez. Tente novamente\n")
            numero = int(input("Segunda tentativa\nQual o número: "))
            if numero == num_r:
                print("Parabéns você acertou o número!\nAté mais!")
                break
            elif numero != num_r:
                print("Infelizmente não foi dessa vez.\nVocê possui só uma chance, pense bem\n")
                numero = int(input("Última tentativa\nQual o número: "))
                if numero == num_r:
                    print("Parabéns, você consegui de última chance!\nQuem sabe na próxima não acerta de primeira, hein.\nAté lá!")
                    break
                else:
                    print(f"Infelizmente você não acertou. O número era {num_r}, uma pena, quem sabe na próxima!")
                    break

    jogarNovamente = input(Fore.BLUE + "Jogar novamente? [Sim/Não]" + Fore.RESET)