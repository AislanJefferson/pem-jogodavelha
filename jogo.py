#!/usr/bin/env python
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
#importa a biblioteca random
import random

#essas funcoes nao sao necessarias, pos podemos tanto preencher quanto limpar
#o tabuleiro usando board = [' '] * 10
'''
def setup_board(board):
	if(len(board)==0):
		for i in range(9):
			board.append(" ")

def clean_board(board):
	for i in range(len(board)):
		board[i] = " "
'''


#Imprime na tela o tabuleiro na forma:
'''
     |   |   
   a | b | c 
  ___|___|___
     |   |   
   d | e | f 
  ___|___|___
     |   |   
   g | h | i 
     |   |
'''
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


#Essa funcao permite que o jogador escolha com qual letra ira jogar
#e no final retorna uma lista, sendo o primeiro elemento a letra do jogador
#e o segundo a letra da cpu
def escolheLetra():
	letter = ' '
	while not (letter == 'X' or letter == 'O'):
		letter = raw_input("Voce deseja jogar como X ou O: ").upper()
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']
		
#escolhe aleatoriamente quem vai ser o primeiro a jogar		
def jogaPrimeiro():
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
		
#funcao que permite ao jogar fazer seu movimento, a funcao verifica se a opcao
#escolhida pelo jogador esta entre as opcoes permitadas e verifica se o espaco esta vazio
def movimentoPlayer(board):
	move = ''
	while move not in ('1 2 3 4 5 6 7 8 9').split() or not verificaEspacoLivre(board, int(move)):
		print('Qual a sua jogada? (1-9)')
		move = raw_input()
	return int(move)

#escreve a letra no tabuleiro			
def fazJogada(board, symbol, move):
	board[move] = symbol

#funcao que pergunta se o jogador deseja jogar novamente
def jogarNovamente():
	print('Voce deseja jogar novamente? (Sim ou Nao)')
	return raw_input().lower().startswith('s')

#Essa funcao verifica todas as possibildiades de vitoria e caso tenha vencedor retorna true
def checaVencedor(board, letter):
	return((board[7] == letter and board[8] == letter and board[9] == letter) or
		(board[4] == letter and board[5] == letter and board[6] == letter) or
		(board[1] == letter and board[2] == letter and board[3] == letter) or
		(board[7] == letter and board[4] == letter and board[1] == letter) or
		(board[8] == letter and board[5] == letter and board[2] == letter) or
		(board[9] == letter and board[6] == letter and board[3] == letter) or
		(board[7] == letter and board[5] == letter and board[3] == letter) or
		(board[9] == letter and board[5] == letter and board[1] == letter))

#Essa funcao cria uma copia do tabuleiro
def copiaBoard(board):
	copyBoard = []
	for i in board:
		copyBoard.append(i)
	return copyBoard

#Verifica se o espaco selecionado esta vazio e retorna true
def verificaEspacoLivre(board, move):
	return board[move] == ' '

#escolhe um movimento valido no tabuleiro
def escolheMovimentoAleatorio(board, movesList):
	possibleMoves = []
	for i in movesList:
		if verificaEspacoLivre(board, i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

#funcao que define a jogada da cpu, utilizando AI
def movimentoCPU(board, computerLetter):
#Dado um tabuleiro e o simbolo do jogador, a funcao determina onde jogar e retorna o movimento
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

# Aqui esta o algoritmo para a AI do jogo da velha
# Primeiro, verificamos se é possivel vencer na proxima jogada
	for i in range(1,10):
		copy = copiaBoard(board)
		if verificaEspacoLivre(copy, i):
			fazJogada(copy, computerLetter, i)
			if checaVencedor(copy, computerLetter):
				return i
				
# Verifica se o jogador pode vencer na proxima jogada e, entao, o bloqueia
	for i in range(1,10):
		copy = copiaBoard(board)
		if  verificaEspacoLivre(copy, i):
			fazJogada(copy, playerLetter, i)
			if checaVencedor(copy, playerLetter):
				return i
# Tenta ocupar algum dos cantos, se eles estiverem livres
	move = escolheMovimentoAleatorio(board, [1,3,7,9])
	if move != None:
		return move
		
# Tenta ocupar o centro, se ele estiver livre
	if verificaEspacoLivre(board, 5):
		return 5
		
#ocupa os lados
	return escolheMovimentoAleatorio(board, [2,4,6,8])

#funcao que verifica se o tabuleiro esta completo e retorna true
def boardCheio(board):
	for i in range(1,10):
		if verificaEspacoLivre(board, i):
			return False
	return True

print ('Bem vindo ao Game da Veia!')						
#Loop principal
while(True):
	#reinicia e zera o tabuleiro, eliminando a necessidade de utilizar funcoes
	theBoard = [' '] * 10
	playerLetter, computerLetter = escolheLetra()
	turn = jogaPrimeiro()
	print('O ' + turn + ' vai jogar primeiro')
	gameIsPlaying = True
	while gameIsPlaying:
		#Vez do jogador fazer sua jogada
		if turn == 'player':
			mostraTabuleiro(theBoard)
			move = movimentoPlayer(theBoard)
			fazJogada(theBoard, playerLetter, move)
			
			#Verifica se ouve vencedor na jogada
			if checaVencedor(theBoard, playerLetter):
				mostraTabuleiro(theBoard)
				print('Parabes! Voce venceu o game!')
				gameIsPlaying = False
			else:
				#Verifica se o tabuleiro esta completo
				if boardCheio(theBoard):
					mostraTabuleiro(theBoard)
					print('O jogo empatou')
					break
				else:
					turn = 'computer'
		else:
			#Vez da CPU fazer sua jogada
			move = movimentoCPU(theBoard, computerLetter)
			fazJogada(theBoard, computerLetter, move)
			
			#verifica se ouve vencedor na jogada
			if checaVencedor(theBoard, computerLetter):
				mostraTabuleiro(theBoard)
				print('O computador venceu o jogo :(')
				gameIsPlaying = False
			else:
				#verifica se o tabuleiro esta completo e sem vencedor
				if boardCheio(theBoard):
					mostraTabuleiro(theBoard)
					print('O jogo empatou!')
					break
				else:
					turn = 'player'
	#pergunta se deseja jogar novamente, se escolher sim o jogo e reiniciado
	if not jogarNovamente():
		break
