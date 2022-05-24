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
    print("-=-==-=-=-==-=-=-==-=--=-=-=-=-=-=-=-=-=-=-=")
    while True:
        for c in range(1,quantidadeJogadores+1): #c→ representa a vez de qual jogador
            palavra= input("Palavra do {}° jogador: \n".format(c))
            print("Caso seja uma palavra dupla precione 2.\n")
            print("Caso seja uma palavra Tripla precione 3. \n")
            palavraEspecial = int(input("Caso não seja nenhuma das duas precione 0: "))
            for l in range(0,len(palavra)): #soma a pontuação de cada jogador em cada rodada
                if c ==1:
                    jogador1Rodada+=letras.valorLetras[palavra[l]]
                if c ==2:
                    jogador2Rodada+= letras.valorLetras[palavra[l]]
                if c ==3:
                    jogador3Rodada+= letras.valorLetras[palavra[l]]
                if c ==4:
                    jogador4Rodada+= letras.valorLetras[palavra[l]]
        #adciona o multiplicador da palavra incial
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
            
            jogador1+= jogador1Rodada
            jogador2+= jogador2Rodada
            jogador3+= jogador3Rodada
            jogador4+= jogador4Rodada
            jogador1Rodada = 0
            jogador2Rodada = 0
            jogador3Rodada = 0
            jogador4Rodada = 0
            bingo = input("Teve bingo?(S/N)")
            if bingo=="S":
                if c == 1:
                    jogador1+=50
                if c == 2:
                    jogador2+=50
                if c == 3:
                    jogador3+=50
                if c == 4:
                    jogador4+=50
            print("-=-==-=-=-==-=-=-==-=--=-=-=-=-=-=-=-=-=-=-=\n")
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