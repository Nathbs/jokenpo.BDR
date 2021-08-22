from random import randint ##busquei a biblioteca para fazer random com numero inteiro
from time import sleep #para dar espaço de tempo entre as jogadas
from Jogada import Jogada ##importando a classe que criei

def bemVindo():
    print("Olá! Seja bem-vindo ao jogo JOKENPO. Vamos jogar?\nPrimeiro vamos revisar a regras!\n"
    "Você deverá escolher um número entre 1,2 e 3, que simbolizará respectivamente Pedra, Papel e Tesoura. \nApós"
    " sua escolha, o computador irá escolher uma opção aleatoriamente. Assim, o computador irá verificar quem é o vencedor"
    " ou se houve empate. \nLembrando que Pedra ganha da tesoura (amassando-a ou quebrando-a), Tesoura ganha do papel "
    "(cortando-o) e Papel ganha da pedra (embrulhando-a).\n 1-Pedra \n 2-Papel \n 3-Tesoura")
    print('-' * 10)

def escolhaDoJogador():
    VerificaEscolhaJogador = int(input("Escolha a sua jogada: ")) ##transformei a string em numero inteiro para poder fazer a verificação
    escolhaValida = False
    while escolhaValida==False:
        if (VerificaEscolhaJogador==1 or VerificaEscolhaJogador==2 or VerificaEscolhaJogador==3): ##comparar se é uma das 3 jogadas possíveis
            escolhaValida = True
            print("Agora é a vez do computador")
        else:
            VerificaEscolhaJogador = int(input("Por favor digite um número válido: ")) ##quando não é uma jogada válida, possibilita que o jogador faça uma nova jogada
    return VerificaEscolhaJogador #gravei o número do humano

def jogadaComputador():
    escolhaComputador = randint(1,3)
    print("A escolha do computador foi: " + str(escolhaComputador)) ##transformei em string a escolha do computador
    return escolhaComputador #gravei o número do computador

def verificarGanhador(escolhaHumano, escolhaMaquina):
    if escolhaMaquina == escolhaHumano: #independente do número, se eles são iguais, dará empate
        print("Houve empate!")
    elif escolhaHumano == 1 and escolhaMaquina == 2: #humano pedra - computador papel
        print("Você perdeu, papel ganha da pedra!")
    elif escolhaHumano == 1 and escolhaMaquina == 3: #humano pedra - computador tesoura
        print("Parabéns, você ganhou! A pedra destroi a tesoura.")
    elif escolhaHumano == 2 and escolhaMaquina == 1: #humano papel - computador pedra
        print("Parabéns, você ganhou! O papel embrulha a pedra.")
    elif escolhaHumano == 2 and escolhaMaquina == 3: #humano papel - computador tesoura
        print("Você perdeu, a tesoura corta o papel!")
    elif escolhaHumano == 3 and escolhaMaquina == 1: #humano tesoura - computador pedra
        print("Você perdeu, a pedra quebra a tesoura!")
    elif escolhaHumano == 3 and escolhaMaquina ==2: #humano tesoura - computador papel
        print("Parabéns, você ganhou! A tesoura corta o papel.")


def jogar():
    novoJogo = '1'
    while novoJogo == '1':
        escolhaHumano = escolhaDoJogador()
        escolhaMaquina = jogadaComputador()
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PO!")
        print('-' * 10)
        verificarGanhador(escolhaHumano, escolhaMaquina)
        print('-' * 10)
        novoJogo = input("Você quer jogar de novo? Digite 1 para sim para jogar novamente ou qualquer caracter para finalizar o jogo: ")

def finalizar():
    print("Obrigada, até a próxima!")

## MAIN NOVO
bemVindo()
jogar()
finalizar()