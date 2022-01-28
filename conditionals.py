
# from multiprocessing import Condition


# devs_money = 100
# dev_can_play_smash = False

# if devs_money > 10 and dev_can_play_smash:
#     print("Dev enters a smash tournament!")

# elif devs_money < 10 and dev_can_play_smash:
#     print("Dev is too poor to enter")    
# else:
#     print("Dev just can't play smash")    


# Conditions exercise

# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"
# p1 = int(input("please input a number: "))
# if p1 > 85 :
#     print("Distinction")
# elif p1 >= 65 and p1<= 85 :
#     print("pass") 

# else: 
#     print("fail")
#OR NESTED IFS with no ELIF's
# if p1 < 85 :
#   if p1 >= 65 and p1<= 85 :
#     print("pass") 
    # else: 
#     print("fail")
# else: 
#     print("Distinction")

#test a number is odd or even (if part of it.. make sure to make nums input of user)
# if num % 2 == 0:
#     pass # Even 
# else:
#     pass # Odd

# In this exercise you will create a program that reads a letter of the alphabet from the user. 
# If the user enters a,e,i,o or u then your program should display a message indicating that the entered letter is a vowel.
#  If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant.
# Otherwise your program should display a message indicating that the letter is a consonant.

letter = input("enter a letter a-z: ")
vowels = ('a','e', 'i','o','u')

if letter in vowels: 
    print(" vowel entered ")
elif letter == 'y':
    print("sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print("letter is a consonant.")    