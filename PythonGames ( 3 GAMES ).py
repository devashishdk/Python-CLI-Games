import os;

'''

#1 GAME : TIC TAC TOE GAME


'''
board = []
for i in range(11):
    board.append(str(i))

def drawBoard():
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def askSides():
    print("Choose Your Sides")
    player1 = ""
    while not(player1 == "X" or player1 == "O"):    
        print("Player 1, Choose : (X or O) >> ")
        player1 = input().upper()
    print("Player 1 is "+player1)
    player2 = ""
    if(player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"
    print("player 2 is "+player2)
    
    return [player1,player2]

def askMove():
    validMoves = []
    for i in range(11):
        validMoves.append(str(i))
    move = 0
    while not(move in validMoves):
        print("Make a move >> " )
        move = input()
    return int(move)

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def gameControllerTICTAC():
    drawBoard()
    sides = askSides()
    turn = "p1"
    p1choice = sides[0]
    p2choice = sides[1]
    gamePlaying = True
    while(gamePlaying):
        if(turn == "p1"):
            print("\nPlayer 1 Turn \n")
            moveIndex = askMove()
            board[moveIndex] = p1choice
            os.system('CLS')
            drawBoard()
            if(isWinner(board,p1choice)):
                print("Player 1 Won")
                print("Press O to exit")
                again = int(input())
                if(again == 1):
                    gamePlaying = False
                else:
                    gamePlaying = False
                    
            turn = "p2"
        elif(turn == "p2"):
            print("\nPlayer 2 Turn \n")
            moveIndex = askMove()
            board[moveIndex] = p2choice
            os.system('CLS')
            drawBoard()
            if(isWinner(board,p2choice)):
                print("Player 2 Won")
                print("Press O to exit")
                again = int(input())
                if(again == 0):
                    gamePlaying = False
                else:
                    gamePlaying = False
            turn = "p1"

'''

#2 GAME : CODEBREAKER

'''

import random

#Storing Numbers In Original List

num_list = []
trials = 0

#Using a loop to append numbers in list
user_guessed_list = []
def num_list_gen():
    a = 1
        
    x = random.sample(range(1, 9), 4)
    
    for i in range (len(x)):
        num_list.append(x[i])

    
def input_number():
    
    global trials
    
    print ("\nGuess The Numbers : ")
    
    while len(user_guessed_list) > 0 : user_guessed_list.pop()

    for i in range(4):
        print("position ",i+1," - ",end="")
        user_guessed_list.append(int(input()))
    
    trials = trials + 1
    print(user_guessed_list)
def input_check():
        
    for i in range(4):
        if (user_guessed_list[i] in num_list and user_guessed_list[i] == num_list[i]):
            print("Y",end = "  ")
        if (user_guessed_list[i] not in num_list):
            print("X",end = "  ")
        if(user_guessed_list[i] in num_list and user_guessed_list[i] != num_list[i]):
            print("O",end = "  ")

def rules():
    print ("there are 4 numbers\n\nyou have to guess them\n\nX ---> The number is not there\n\nO ---> The number is there but in different position\n\nY ---> The number is there and in Correct Position\n\nYou have to guess the numbers")

def CodeBreaker():
    print("Welcome To The Game\n\n")
    rules()
    num_list_gen()
    while(user_guessed_list != num_list):
        input_number()
        print(" ",end="")
        input_check() 
        
    print("\n\nYou Won The Game in ", trials ," Trials")

    print("\n\nThank u For playing the game \n\npress [Enter] to exit")

    play = input()   



'''

#3 GAME : GUESS THE NUMBER 

'''


def GuessNumber():
	original_no = random.randint(1,9)
	print("You Have 3 trials to guess a number between 1-9\n\n")

	guessed_no = int(input("Guess the number : "))
	trials = 1
	status = 0
	while(original_no != guessed_no):
	    if (trials > 2):
	        print("\n\nYou Lost\n\nAnd the number is : ",original_no,"\n\n")
	        
	        original_no = guessed_no
	        status = 1
	        
	    else:
	        guessed_no = int(input("Guess the number : "))
	        trials = trials + 1
	if (status == 0):
	    print("\n\nCongratulation you won the game in ",trials," Trials")
	    
	    
	x = input("Press [Enter] to exit the game")




print("CHOOSE THE GAME YOUR WANT TO PLAY\n"+
        "1. TIC TAC TOE\n"+
        "2. CODE BREAKER"+
        "3. GUESS THE NUMBER\n"
            +"CHOOSE A NUMBER (1 , 2 , 3)")

choiceGame = int(input())

if(choiceGame == 1):
    gameControllerTICTAC()
elif(choiceGame == 2):
    CodeBreaker()
elif(choiceGame == 3):
    GuessNumber()
else:
    print("NOT THE CORRECT CHOICE CHOOSE BETWEEN 1, 2 , 3")
    