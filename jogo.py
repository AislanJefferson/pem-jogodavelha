#!/usr/bin/env python3

"""Jogo da velha - Aula GIT - PEM

Descricao:
    Jogo da velha em interface grafica em linha de comando
     com dois modos: Contra o computador (utilizando o algoritmo minimax)
     e contra um adversario via rede.
TODO:
    -Tudo!

Autores:
    Aislan Jefferson - aislanjsb@gmail.com
    Douglas Nickson - douglas.nickson1@gmail.com
    Laerty Santos - laerty.santos@gmail.com
    Willian Klein - williannene1@hotmail.com

"""

import random

tGame = int(input("Voce deseja jogar: \n1 - OFFLINE \n2 - MULTIPLAYER\n"))

if tGame == 1:
	def mostraTabuleiro(board):
		print("   |   |   ")
		print(" {} | {} | {} ".format(board[7],board[8],board[9]))
		print("___|___|___")
		print("   |   |   ")
		print(" {} | {} | {} ".format(board[4],board[5],board[6]))
		print("___|___|___")
		print("   |   |   ")
		print(" {} | {} | {} ".format(board[1],board[2],board[3]))
		print("   |   |   ")

	def escolheLetra():
		letter = ' '
		while not (letter == 'X' or letter == 'O'):
			letter = input("Voce deseja jogar como X ou O: ").upper()
		if letter == 'X':
			return ['X', 'O']
		else:
			return ['O', 'X']
			
	def jogaPrimeiro():
		if random.randint(0,1) == 0:
			return 'computer'
		else:
			return 'player'

	def movimentoPlayer(board):
		move = ''
		while move not in ('1 2 3 4 5 6 7 8 9').split() or not verificaEspacoLivre(board, int(move)):
			print('Qual a sua jogada? (1-9)')
			move = input()
		return int(move)
				
	def fazJogada(board, symbol, move):
		board[move] = symbol

	def jogarNovamente():
		print('Voce deseja jogar novamente? (Sim ou Nao)')
		return input().lower().startswith('s')

	def montaTabuleiro(board):
		if(len(board)==0):
			for i in range(9):
				board.append(" ")

	def checaVencedor(board, letter):
		return((board[7] == letter and board[8] == letter and board[9] == letter) or
			(board[4] == letter and board[5] == letter and board[6] == letter) or
			(board[1] == letter and board[2] == letter and board[3] == letter) or
			(board[7] == letter and board[4] == letter and board[1] == letter) or
			(board[8] == letter and board[5] == letter and board[2] == letter) or
			(board[9] == letter and board[6] == letter and board[3] == letter) or
			(board[7] == letter and board[5] == letter and board[3] == letter) or
			(board[9] == letter and board[5] == letter and board[1] == letter))

	def copiaBoard(board):
		copyBoard = []
		for i in board:
			copyBoard.append(i)
		return copyBoard

	def verificaEspacoLivre(board, move):
		return board[move] == ' '

	def escolheMovimentoAleatorio(board, movesList):
		possibleMoves = []
		for i in movesList:
			if verificaEspacoLivre(board, i):
				possibleMoves.append(i)
		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None

	def movimentoCPU(board, computerLetter):
		if computerLetter == 'X':
			playerLetter = 'O'
		else:
			playerLetter = 'X'

		for i in range(1,10):
			copy = copiaBoard(board)
			if verificaEspacoLivre(copy, i):
				fazJogada(copy, computerLetter, i)
				if checaVencedor(copy, computerLetter):
					return i

		for i in range(1,10):
			copy = copiaBoard(board)
			if  verificaEspacoLivre(copy, i):
				fazJogada(copy, playerLetter, i)
				if checaVencedor(copy, playerLetter):
					return i

		move = escolheMovimentoAleatorio(board, [1,3,7,9])
		if move != None:
			return move

		if verificaEspacoLivre(board, 5):
			return 5

		return escolheMovimentoAleatorio(board, [2,4,6,8])

	def boardCheio(board):
		for i in range(1,10):
			if verificaEspacoLivre(board, i):
				return False
		return True

	print ('Bem vindo ao Game da Veia!')						
	#Loop principal
	while(True):
		theBoard = [' '] * 10
		playerLetter, computerLetter = escolheLetra()
		turn = jogaPrimeiro()
		print('O ' + turn + ' vai jogar primeiro')
		gameIsPlaying = True
		while gameIsPlaying:
			if turn == 'player':
				mostraTabuleiro(theBoard)
				move = movimentoPlayer(theBoard)
				fazJogada(theBoard, playerLetter, move)

				if checaVencedor(theBoard, playerLetter):
					mostraTabuleiro(theBoard)
					print('Parabes! Voce venceu o game!')
					gameIsPlaying = False
				else:
					if boardCheio(theBoard):
						mostraTabuleiro(theBoard)
						print('O jogo empatou')
						break
					else:
						turn = 'computer'
			else:
				move = movimentoCPU(theBoard, computerLetter)
				fazJogada(theBoard, computerLetter, move)

				if checaVencedor(theBoard, computerLetter):
					mostraTabuleiro(theBoard)
					print('O computador venceu o jogo :(')
					gameIsPlaying = False
				else:
					if boardCheio(theBoard):
						mostraTabuleiro(theBoard)
						print('O jogo empatou!')
						break
					else:
						turn = 'player'

		if not jogarNovamente():
			break
	
else:
	print('MULTIPLAYER')
		
