from letras import letras


def contador (quantidadeJogadores):
    jogador1Rodada =0
    jogador2Rodada =0
    jogador3Rodada =0
    jogador4Rodada =0
        
    jogador1 =0
    jogador2 =0
    jogador3 =0
    jogador4 =0 
    while True:
        #c→ representa a vez de qual jogador
        for c in range(1,quantidadeJogadores+1): 
            palavra= input("Palavra do {}° jogador: \n".format(c))
            letraEspecial = input("Qual é  a letra especial?(caso nenhuma aperte y) ")
            
            #soma a pontuação de cada jogador em cada rodada
            for l in range(0,len(palavra)): 
                if c ==1:
                    #adciona apontuação de letra especial
                    if letraEspecial !="y":
                        if letraEspecial == palavra[l]:
                            valorMult = int(input("Qual é o multiplicador:"))
                            jogador1Rodada = letras.valorLetras[letraEspecial]*valorMult
                            jogador1Rodada -= letras.valorLetras[letraEspecial]
                    jogador1Rodada+=letras.valorLetras[palavra[l]]

                if c ==2:
                    #adciona apontuação de letra especial
                    if letraEspecial !="y":
                        if letraEspecial == palavra[l]:
                            valorMult = int(input("Qual é o multiplicador:"))
                            jogador2Rodada = letras.valorLetras[letraEspecial]*valorMult
                            jogador2Rodada -= letras.valorLetras[letraEspecial]
                    jogador2Rodada+= letras.valorLetras[palavra[l]]
                if c ==3:
                    #adciona apontuação de letra especial
                    if letraEspecial !="y":
                        if letraEspecial == palavra[l]:
                            valorMult = int(input("Qual é o multiplicador:"))
                            jogador3Rodada = letras.valorLetras[letraEspecial]*valorMult
                            jogador3Rodada -= letras.valorLetras[letraEspecial]
                    jogador3Rodada+= letras.valorLetras[palavra[l]]
                if c ==4:
                    #adciona apontuação de letra especial
                    if letraEspecial !="y":
                        if letraEspecial == palavra[l]:
                            valorMult = int(input("Qual é o multiplicador:"))
                            jogador4Rodada = letras.valorLetras[letraEspecial]*valorMult
                            jogador4Rodada -= letras.valorLetras[letraEspecial]
                    jogador4Rodada+= letras.valorLetras[palavra[l]]
        #adciona os multiplicadores de palavras especiais
            print("Caso seja uma palavra dupla precione 2.\n")
            print("Caso seja uma palavra Tripla precione 3. \n")
            palavraEspecial = int(input("Caso não seja nenhuma das duas precione 0: "))
            if palavraEspecial==0:
                pass
            if c==1:
                if palavraEspecial==0:
                    pass
                if palavraEspecial==2:
                    jogador1Rodada*=2
                if palavraEspecial==3:
                    jogador1Rodada*=3
            if c==2:
                if palavraEspecial==0:
                    pass
                if palavraEspecial==2:
                    jogador2Rodada*=2
                if palavraEspecial==3:
                    jogador2Rodada*=3
            if c==3:
                if palavraEspecial==0:
                    pass
                if palavraEspecial==2:
                    jogador3Rodada*=2
                if palavraEspecial==3:
                    jogador3Rodada*=3      
            if c==4:
                if palavraEspecial==0:
                    pass
                if palavraEspecial==2:
                    jogador4Rodada*=2
                if palavraEspecial==3:
                    jogador4Rodada*=3
        
        print(jogador1Rodada)
        #adciona a pontuação da rodada a puntuação geral e zera a pontuação da rodada
        jogador1+= jogador1Rodada
        jogador2+= jogador2Rodada
        jogador3+= jogador3Rodada
        jogador4+= jogador4Rodada
        jogador1Rodada = 0
        jogador2Rodada = 0
        jogador3Rodada = 0
        jogador4Rodada = 0

        #adciona a pontuação bingo
        bingo = input("Teve bingo?(S/N)")
        if bingo=="S":
            qualJogador = int(input("Qual é  o numero do jogador que teve bingo?"))
            if qualJogador == 1:
                jogador1+=50
            if qualJogador == 1:
                jogador2+=50
            if qualJogador == 1:
                jogador3+=50
            if qualJogador == 1:
                jogador4+=50
        fimJogo = input("O jogo acabou?(s/n)")
        if fimJogo== "s":
            if quantidadeJogadores==1:
                print("pontuação do jogador 1: {}".format(jogador1))
            elif quantidadeJogadores==2: 
                print("pontuação do jogador 1: {}".format(jogador1))
                print("pontuação do jogador 2: {}".format(jogador2))
            elif quantidadeJogadores==3: 
                print("pontuação do jogador 1: {}".format(jogador1))
                print("pontuação do jogador 2: {}".format(jogador2))
                print("pontuação do jogador 3: {}".format(jogador3))
            else: 
                print("pontuação do jogador 1: {}".format(jogador1))
                print("pontuação do jogador 2: {}".format(jogador2))
                print("pontuação do jogador 3: {}".format(jogador3))
                print("pontuação do jogador 4: {}".format(jogador4))


 
            break