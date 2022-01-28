
#Q3)
# Write a Python program to guess a number between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again 
# until the guess is correct, on successful guess, user will get 
# a "Well guessed!" message, and the program will exit.

# import pdb
# pdb.set_trace()

# from random import randrange


# def playGuess() : 

#     randomNum = randrange(10)  # random number 1 to 10
#     print(randomNum)
#     userGuess = 0; # starting point

#     while userGuess != randomNum : 
#             userGuess = int(input("please guess a number between 0-10: ")) 
#             if userGuess == randomNum :
#                 print("well guessed!")



# playGuess()    



#Q4)
# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 

# import pdb
# pdb.set_trace()

# start = 5 # can replace 5 with start
# for i in range(5):
#         for j in range(i):
#             print("* ", end = " ") #print end=" " will stop going printing horizontally but vertically e.g. 5 hori 4 hori etc. but now 5 ver 5 ver etc..
#         print("")  # creates a new line

# for i in range(5 ,0,-1): # range from 5-0 (not including 0) , reverse with -1
# 	    for j in range(i):
# 	        print("* ", end = " ")    #print end=" " will stop going printing horizontally but vertically e.g. 5 hori 4 hori etc. but now 5 ver 5 ver etc..
# 	    print('')  # creates a new line or can have "\n"


# Q5). Write a Python program that accepts a word from the user and reverse it.

# userInput = input("enter your name: ")
# # print(userInput)
# for i in range(len(userInput) -1, -1, -1):   ## first -1 starts string from end, 2nd and 3rd help loop count reversly therefore reverse found
#     print(userInput[i], end =" ")  ## end=... helps output vertically rather than horizontally





