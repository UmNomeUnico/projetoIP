import minhaBib
import time

deckPlayer1 = []
deckPlayer2 = []
deckCentral = []
lista = []

vidaP1 = 1000
vidaP2 = 1000

quantCartasJogadores = 4
rodadas = 4
tutorial = 0

diferenca = 0
iniciar = "s"
continuar = "s"
tutorialMostrar = ""
vencedor = ""
perdedor = ""
vida = ""
vidaV = ""
vidaP = ""
playerComparacao = ""
empate = False

print("""                                                                                       
                                                                                                                                                                       dddddddd
                                        PPPPPPPPPPPPPPPPP                    kkkkkkkk                               DDDDDDDDDDDDD                                      d::::::d
                                        P::::::::::::::::P                   k::::::k        \033[34m\033[1mUFPB CAMPUS IV\033[0m         D::::::::::::DDD                                   d::::::d
                                        P::::::PPPPPP:::::P                  k::::::k                               D:::::::::::::::DD                                 d::::::d
                                        PP:::::P     P:::::P                 k::::::k                               DDD:::::DDDDD:::::D                                d:::::d 
                                          P::::P     P:::::P   ooooooooooo    k:::::k    kkkkkkk    eeeeeeeeeeee      D:::::D    D:::::D   aaaaaaaaaaaaa       ddddddddd:::::d 
                                          P::::P     P:::::P oo:::::::::::oo  k:::::k   k:::::k   ee::::::::::::ee    D:::::D     D:::::D  a::::::::::::a    dd::::::::::::::d 
                                          P::::PPPPPP:::::P o:::::::::::::::o k:::::k  k:::::k   e::::::eeeee:::::ee  D:::::D     D:::::D  aaaaaaaaa:::::a  d::::::::::::::::d 
                                          P:::::::::::::PP  o:::::ooooo:::::o k:::::k k:::::k   e::::::e     e:::::e  D:::::D     D:::::D           a::::a d:::::::ddddd:::::d 
                                          P::::PPPPPPPPP    o::::o     o::::o k::::::k:::::k    e:::::::eeeee::::::e  D:::::D     D:::::D    aaaaaaa:::::a d::::::d    d:::::d 
                                          P::::P            o::::o     o::::o k:::::::::::k     e:::::::::::::::::e   D:::::D     D:::::D  aa::::::::::::a d:::::d     d:::::d 
                                          P::::P            o::::o     o::::o k:::::::::::k     e::::::eeeeeeeeeee    D:::::D     D:::::D a::::aaaa::::::a d:::::d     d:::::d 
                                          P::::P            o::::o     o::::o k::::::k:::::k    e:::::::e             D:::::D    D:::::D a::::a    a:::::a d:::::d     d:::::d 
                                        PP::::::PP          o:::::ooooo:::::ok::::::k k:::::k   e::::::::e          DDD:::::DDDDD:::::D  a::::a    a:::::a d::::::ddddd::::::dd
                                        P::::::::P          o:::::::::::::::ok::::::k  k:::::k   e::::::::eeeeeeee  D:::::::::::::::DD   a:::::aaaa::::::a  d:::::::::::::::::d
                                        P::::::::P           oo:::::::::::oo k::::::k   k:::::k   ee:::::::::::::e  D::::::::::::DDD      a::::::::::aa:::a  d:::::::::ddd::::d
                                        PPPPPPPPPP             ooooooooooo   kkkkkkkk    kkkkkkk    eeeeeeeeeeeeee  DDDDDDDDDDDDD          aaaaaaaaaa  aaaa   ddddddddd   ddddd
""")
time.sleep(2)
print("")
print("")
print("Bem vindo, Para uma melhor experiencia amplie o terminal para tela cheia 😁!!!")
print("")
print("informe os nomes dos jogadores:")
print("")

while(continuar == "s"):
        time.sleep(1)
        player1 = str(input("Digite o nome do jogador 1🎮: ")) #nome player
        player2 = str(input("Digite o nome do jogador 2🎮: ")) #nome player
        tutorial = str.lower(input("Gostaria de ver o tutorial? (s/n)"))#mostrar tutorial

        if(tutorial == "s"):
            tutorialMostrar = minhaBib.tutorial(tutorialMostrar)
        while(tutorial != "s") and (tutorial != "n"):  #laço de repetição para usuario chato
          print("Letra inválida! Tente outra vez.😃")    #laço de repetição para usuario chato
          tutorial = str.lower(input("Devo mostrar o tutorial?✎ (s/n)"))    #laço de repetição para usuario chato

        deckEmbaralhado = minhaBib.card_valor(lista)#embaralhando caracteristicas e nome das cartas


        deckPlayer1, deckPlayer2, deckEmbaralhado = minhaBib.embaralhar(deckPlayer1, deckPlayer2, deckEmbaralhado) #embaralhando deck para começar a jogar
        print("")
        print("É hora do duuueeeelo!!! dududu, chegou sua vez!🤺")
        print("")
        time.sleep(2)#2 segundos para iniciar



        #for i in range(rodadas):
        count = 4
        while (count):

            while True: #laço de repetição para usuario chato
                try: #laço de repetição para usuario chato
                    if(rodadas % 2 == 0):
                        playerComparacao = int(input(f"{player1}, digite qual caracteristica da sua carta você deseja comparar:  \033[1m1(Ataque⚔️)2|(Defesa🛡️)|3(Velocidade👟):\033[0m  "))

                    else:
                        playerComparacao = int(input(f"{player2}, digite qual caracteristica da sua carta você deseja comparar:  \033[1m1(Ataque⚔️)|2(Defesa🛡️)|3(Velocidade👟):\033[0m  ")) #laço de repetição para usuario chato

                    while(playerComparacao != 1) and (playerComparacao != 2) and (playerComparacao != 3): #laço de repetição para usuario chato
                        print("Número diferente dos pedidos, por favor digite o número correto correspondente a caracteristica.😃") #laço de repetição para usuario chato
                        playerComparacao = int(input("Digite qual caracteristica você deseja comparar:  1(Ataque⚔️) 2(Defesa🛡️) 3(Velocidade👟): ")) #laço de repetição para usuario chato
                except ValueError: #laço de repetição para usuario chato
                    print("Digite apenas números😃") #laço de repetição para usuario chato
                    continue #laço de repetição para usuario chato
                break #laço de repetição para usuario chato

            if(playerComparacao == 1):#comparação com 1 caracteristica ataque
                empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2 = minhaBib.comparar1(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2)
                if(empate):
                    count
                else:
                    count -= 1

            elif(playerComparacao == 2):#comparação com 2 caracteristica defesa
                empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2 = minhaBib.comparar2(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2)
                if (empate):
                    count
                else:
                    count -= 1
            elif(playerComparacao == 3):#comparação com 3 caracteristica velocidade
                empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2 = minhaBib.comparar3(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2)
                if (empate):
                    count
                else:
                    count -= 1
            # vencedor/perdedor
        vencedor, perdedor, vida = minhaBib.vencedor(player1, player2, vidaP1, vidaP2, perdedor)

        print(f"{vencedor}\n{perdedor} ")

        continuar = str.lower(input("Quer tentar novamente?✎ (s/n)"))#jogar novamente
        while (continuar != "s") and (continuar != "n"): #laço de repetição para usuario chato
            print("Letra inválida! Tente outra vez.") #laço de repetição para usuario chato
            continuar = str.lower(input("Deseja continuar? (s/n) ")) #laço de repetição para usuario chato
        if (continuar == "s"):
            continuar = "s"

            deckPlayer1.clear()
            deckPlayer2.clear()
            deckEmbaralhado.clear()
            vidaP1 = 1000
            vidaP2 = 1000

            print("O jogo vai recomeçar!")
            print("")

print("")
print("Projeto UFPB \033[34m\033[1mCampus IV LCC\033[0m: introdução a programação, Feito por: Fernando Guilherme de Carvalho, Aline jesuino santos, Lucas Felipe Gomes Pedrosa")
print("Observação: l.c.c melhor que s.i!")
print("")