from letras import letras

jogador1 =0
jogador2 =0
jogador3 =0
jogador4 =0


quantidadeJogadores = int(input("quantos jogadores serão? "))

while True:
    for c in range(1,quantidadeJogadores+1): #c→ representa a vez de qual jogador
        palavra= input("Palavra do {}° jogador: \n".format(c))
        print("Caso seja uma palavra dupla precione 2.\n")
        print("Caso seja uma palavra Tripla precione 3. \n")
        palavraEspecial = int(input("Caso não seja nenhuma das duas precione 0: "))
        
        #isso soma o valor de cada letra
        for l in range(0,len(palavra)):
            if c ==1:
                jogador1+=letras.valorLetras[palavra[l]]
            if c ==2:
                jogador2+= letras.valorLetras[palavra[l]]
            if c ==3:
                jogador3+= letras.valorLetras[palavra[l]]
            if c ==4:
                jogador4+= letras.valorLetras[palavra[l]]
        if palavraEspecial==0:
            pass
        
        # isso multiplica a palavra do jogador . Preciso colocar isso em outro arquivo
        if c==1:
            if palavraEspecial==0:
                pass
            if palavraEspecial==2:
                jogador1*=2
            if palavraEspecial==3:
                jogador1*=3
        if c==2:
            if palavraEspecial==0:
                pass
            if palavraEspecial==2:
                jogador2*=2
            if palavraEspecial==3:
                jogador2*=3
        if c==3:
            if palavraEspecial==0:
                pass
            if palavraEspecial==2:
                jogador3*=2
            if palavraEspecial==3:
                jogador3*=3      
        if c==4:
            if palavraEspecial==0:
                pass
            if palavraEspecial==2:
                jogador4*=2
            if palavraEspecial==3:
                jogador4*=3                                          
    fimJogo = input("O jogo acabou?(s/n)")
    if fimJogo== "s":
        print("pontuação do jogador1 {}".format(jogador1))
        print("pontuação do jogador2 {}".format(jogador2))
        print("pontuação do jogador3 {}".format(jogador3))
        print("pontuação do jogador4 {}".format(jogador4))
        break
                


    

