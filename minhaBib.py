def card_valor(lista):
    import random

    # Listas
    teste = lista
    lista = []
    quantVezes = 20
    embaralhar_Card = 1

    nome = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Rattata", "Spearow", "Ekans",
            "Pikachu", "Sandshrew", "Nidoran", "Clefairy", "Vulpix", "Jigglepuff", "Oddish", "Paras", "Diglett",
            "Meowth",
            "Psyduck", "Mankey"]

    for i in range(embaralhar_Card):
        random.shuffle(nome)
        for i in range(quantVezes):  # random caracteristicas dos pokemons
            ataque = random.randint(1, 100)
            teste.append(ataque)
            defesa = random.randint(1, 100)
            teste.append(defesa)
            velocidade = random.randint(1, 100)
            teste.append(velocidade)
            teste.insert(0, nome[i])
            lista.append(teste[:])
            teste.clear()

    return lista


def embaralhar(deckPlayer1, deckPlayer2, deckEmbaralhado,):
    deckPlayer1 = deckPlayer1
    deckPlayer2 = deckPlayer2
    deckEmbaralhado = deckEmbaralhado
    quantCartasJogadores = 4

    for i in range(quantCartasJogadores):  # quantidade de cartas de cada jogador
        deckPlayer1.append(deckEmbaralhado[i])
        del (deckEmbaralhado[i])
        deckPlayer2.append(deckEmbaralhado[i])
        del (deckEmbaralhado[i])

    return deckPlayer1, deckPlayer2, deckEmbaralhado


def comparar1(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidap1, vidap2, player1, player2):
    ####LISTAS####
    deckPlayer1 = deckPlayer1
    deckPlayer2 = deckPlayer2
    deckEmbaralhado = deckEmbaralhado
    vidaP1 = vidap1
    vidaP2 = vidap2

    ################comparação#####################
    if (deckPlayer1[0][1]) > (deckPlayer2[0][1]):
        print("")
        print(f"{deckPlayer1[0][0]}😁 venceu do {deckPlayer2[0][0]}😔")

        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer1[0][1] - deckPlayer2[0][1]
        vidaP1 += deckPlayer1[0][1]
        vidaP2 -= diferenca
        deckPlayer1.append(deckPlayer2[0])
        del deckPlayer2[0]

    elif (deckPlayer1[0][1]) < (deckPlayer2[0][1]):
        print("")
        print(f"{deckPlayer1[0][0]}😔 perdeu para o {deckPlayer2[0][0]}😁")

        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer2[0][1] - deckPlayer1[0][1]
        vidaP2 += deckPlayer2[0][1]
        vidaP1 -= diferenca
        deckPlayer2.append(deckPlayer1[0])
        del deckPlayer1[0]

    elif (deckPlayer1[0][1]) == (deckPlayer2[0][1]):
        print("")
        print(f"{deckPlayer1[0][0]}😱 empatou com {deckPlayer2[0][0]}😱")

        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")


        del deckPlayer1[0]
        del deckPlayer2[0]
        deckPlayer1.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        deckPlayer2.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        empate = True

    return empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2


def comparar2(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidap1, vidap2, player1, player2):
    ####LISTAS####
    deckPlayer1 = deckPlayer1
    deckPlayer2 = deckPlayer2
    deckEmbaralhado = deckEmbaralhado
    vidaP1 = vidap1
    vidaP2 = vidap2

    if (deckPlayer1[0][2]) > (deckPlayer2[0][2]):
        print("")
        print(f"{deckPlayer1[0][0]}😁 venceu do {deckPlayer2[0][0]}😔")

        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer1[0][2] - deckPlayer2[0][2]
        vidaP1 += deckPlayer1[0][2]
        vidaP2 -= diferenca
        deckPlayer1.append(deckPlayer2[0])
        del deckPlayer2[0]

    elif (deckPlayer1[0][2]) < (deckPlayer2[0][2]):
        print(f"")
        print(f"{deckPlayer1[0][0]}😔 perdeu para o {deckPlayer2[0][0]}😁")

        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer2[0][2] - deckPlayer1[0][2]
        vidaP2 += deckPlayer2[0][2]
        vidaP1 -= diferenca
        deckPlayer2.append(deckPlayer1[0])
        del deckPlayer1[0]

    elif (deckPlayer1[0][2]) == (deckPlayer2[0][2]):

        print("")
        print(f"{deckPlayer1[0][0]}😱 empatou com {deckPlayer2[0][0]}😱")
        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        del deckPlayer1[0]
        del deckPlayer2[0]
        deckPlayer1.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        deckPlayer2.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        empate = True

    return empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2


def comparar3(empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidap1, vidap2, player1, player2):
    deckPlayer1 = deckPlayer1
    deckPlayer2 = deckPlayer2
    deckEmbaralhado = deckEmbaralhado
    vidaP1 = vidap1
    vidaP2 = vidap2

    if (deckPlayer1[0][3]) > (deckPlayer2[0][3]):

        print("")
        print(f"{deckPlayer1[0][0]}😁 venceu do {deckPlayer2[0][0]}😔")
        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer2[0][3] - deckPlayer1[0][3]
        vidaP1 += deckPlayer1[0][3]
        vidaP2 -= diferenca
        deckPlayer1.append(deckPlayer2[0])
        del deckPlayer2[0]

    elif (deckPlayer1[0][3]) < (deckPlayer2[0][3]):

        print("")
        print(f"{deckPlayer1[0][0]}😔 perdeu para o {deckPlayer2[0][0]}😁")
        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        diferenca = deckPlayer2[0][3] - deckPlayer1[0][3]
        vidaP2 += deckPlayer2[0][3]
        vidaP1 -= diferenca
        deckPlayer2.append(deckPlayer1[0])
        del deckPlayer1[0]

    elif (deckPlayer1[0][3]) == (deckPlayer2[0][3]):
        print("")

        print(f"{deckPlayer1[0][0]}😱 empatou com {deckPlayer2[0][0]}😱")
        print(f"")
        print(f"Carta de: \033[35m{player1}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer1[0][0]}    ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer1[0][1]}    ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer1[0][2]}    ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer1[0][3]}    ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print(f"")
        print(f"Carta de: \033[36m{player2}")
        print(f"\033[0;0m▓≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print(f"\033[1;33mNome📇:{deckPlayer2[0][0]}  ")
        print(f"\033[1;31mAtaque⚔️︎:{deckPlayer2[0][1]}  ")
        print(f"\033[1;34mDefesa🛡️:{deckPlayer2[0][2]}  ")
        print(f"\033[1;32mVelocidade👟:{deckPlayer2[0][3]}   ")
        print(f"\033[0;0m≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡▓")
        print("")

        del deckPlayer1[0]
        del deckPlayer2[0]
        deckPlayer1.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        deckPlayer2.insert(0, deckEmbaralhado[0])
        del deckEmbaralhado[0]
        empate = True


    return empate, deckPlayer1, deckPlayer2, deckEmbaralhado, vidaP1, vidaP2, player1, player2


def vencedor(player1, player2, vidaP1, vidaP2, vida):
    vencedor = ""
    perdedor = ""

    if (vidaP1 > vidaP2):  # substituir por função
        vencedor = str(f"👯🎇O vencedor foi {player1}, com a vida:{vidaP1}👯‍♀️🥳")
        perdedor = str(f"💫O perdedor é:{player2} 😪, com total de vida:{vidaP2} 💫")
    elif (vidaP1 < vidaP2):
        vencedor = str(f"👯🎇 O vencedor foi {player2}, com a vida:{vidaP2} 👯‍♀️🥳")
        perdedor = str(f"💫 O perdedor foi {player1} 😪, com a vida:{vidaP1} 💫")
    elif (vidaP1 == vidaP2):
        vencedor = str(f"empate!!💩, a vida de {player1} ficou:{vidaP1}, a vida de {player2} ficou:{vidaP2}")
        perdedor = ""

    return vencedor, perdedor, vida


def tutorial(a):
    return print("""Tutorial:
                          1 - O jogo terá dois participantes. Inicialmente, cada um começa com 1000 pontos, e 4 cartas sorteadas aleatoriamente do baralho,
                          que ficarão empilhadas e ocultas , as demais cartas ficam ocultas em uma pilha central.

                          2 - A cada rodada, os participantes se alternam escolhendo uma das características para desafiar seu oponente. As cartas de cima da pilha de cada um 
                          terão os valores dessa característica comparados, e aquele que tiver maior valor ganha a rodada.

                          3 - O jogador vencedor terá sua pontuação aumentada do valor da característica vencedora. Já o jogador perdedor da rodada terá sua pontuação diminuída pela
                          diferença entre os valores comparados nas cartas. (Ex: considerando a característica velocidade, caso a carta do Jogador 1 tenha valor 100 e a do 
                          Jogador 2 tenha valor 20, o Jogador 1 ganhará 100 pontos e o Jogador 2 perderá 80 pontos). Em caso de empate nos valores, a rodada é anulada e as cartas
                          são descartadas. Então, cada jogador recebe uma nova carta dentre as que ficaram na pilha central, iniciando a rodada novamente com a escolha da característica
                          a ser comparada

                          4 - Após 4 rodadas, vencerá o jogador que tiver o maior saldo de pontos. Caso ambos tenham o mesmo saldo, será decretado um empate.


                                                                                      Bom jogo!""")
print("")