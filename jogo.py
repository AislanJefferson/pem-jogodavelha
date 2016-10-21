# funcao que define a jogada da cpu, utilizando AI
def movimentoCPU(board, computerLetter):
    # Dado um tabuleiro e o simbolo do jogador, a funcao determina onde jogar e retorna o movimento
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Aqui esta o algoritmo para a AI do jogo da velha
    # Primeiro, verificamos se é possivel vencer na proxima jogada
    for i in range(1, 10):
        copy = copiaBoard(board)
        if verificaEspacoLivre(copy, i):
            fazJogada(copy, computerLetter, i)
            if checaVencedor(copy, computerLetter):
                return i

                # Verifica se o jogador pode vencer na proxima jogada e, entao, o bloqueia
    for i in range(1, 10):
        copy = copiaBoard(board)
        if verificaEspacoLivre(copy, i):
            fazJogada(copy, playerLetter, i)
            if checaVencedor(copy, playerLetter):
                return i
                # Tenta ocupar algum dos cantos, se eles estiverem livres
    move = escolheMovimentoAleatorio(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Tenta ocupar o centro, se ele estiver livre
    if verificaEspacoLivre(board, 5):
        return 5

    # ocupa os lados
    return escolheMovimentoAleatorio(board, [2, 4, 6, 8])
