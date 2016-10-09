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

#Defino o tabuleiro como uma lista com 9 itens
# representando o teclado numerico de 1 a 9
board = []

#Funcao para preencher com itens vazios, representados por espaco
# em branco(" "), no tabuleiro vazio
def setup_board(board):
	if(len(board)==0):
		for i in range(9):
			board.append(" ")

#Funcao para limpeza do tabuleiro para caso deseje jogar novamente			
def clean_board(board):
	for i in range(len(board)):
		board[i] = " "

#Inicio das funcoes relativas a mecanica do jogo

#Imprime na tela o tabuleiro na forma:
#     |   |   
#   a | b | c 
#  ___|___|___
#     |   |   
#   d | e | f 
#  ___|___|___
#     |   |   
#   g | h | i 
#     |   |
def print_board(board):
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[6],board[7],board[8]))
	print("___|___|___")
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[3],board[4],board[5]))
	print("___|___|___")
	print("   |   |   ")
	print(" {} | {} | {} ".format(board[0],board[1],board[2]))
	print("   |   |   ")

#Funcao que checa se o movimento desejado esta livre ou nao, 
# por se tratar de uma lista que o indice comeca com zero, 
# temos de tratar para adaptar ao jogo.
def is_space_free(board, move):
	index = move - 1  #Adaptacao do movimento ao indice de board
	return board[index] == " "

#Funcao que insere o caractere no tabuleiro, por se tratar
# de uma lista que o indice comeca com zero, temos de tratar
# para adaptar ao jogo.
def make_move(board, move, symbol):
	index = move - 1  #Adaptacao do movimento ao indice de board
	board[index] = symbol

#Loop principal
while(True):
	#Conteudo desse bloco ateh agora eh apenas para desenvolvimento
	#Configura o tabuleiro, faz um movimento e imprime na tela
	#Estou com duvida se crio o board apenas aqui dentro...
	setup_board(board)
	make_move(board, 5, "X")
	print_board(board)
	# Testa a funcao is_space_free para o primeiro elemento
	assert not(is_space_free(board,5)), "Item do meio deveria estar ocupado... :("
	print("OK. A implentar o resto...")
	break