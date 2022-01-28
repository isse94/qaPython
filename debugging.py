import pdb

pdb.set_trace()


# qa excercise
#ex1

# user_funds = 10.31
# item_price = (price["Burger"]) #price is not defined

# if item_price < user_funds:
#     Print("You have enough money!") # p instead of P
# if item_price = user_funds: # should be ==
#     print("You have the precise amount of money") 
# if item_price < user_funds:
#     print(Sorry you don't have enough money) #missing ""

 #ex2 
#  def product(n): #unexpected indentation
#     total == 1 ##total not defined
#     for n in n:
#         total *= i ##total not defined
# return total       #can only be used with a function / indentation error

# print(product([4,4,5]))

#ex3 
# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n = 0:   ##missing ==
#                 return False
#             return True             ##no else statement


#ex4
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])  #TypeError: list indices must be integers or slices, not str

print (item_list[5]) # missing ()