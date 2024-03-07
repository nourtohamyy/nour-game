#github Username : nourtohamyy  
#purpose : subtract square game
#Author : nour eldin hany mohamed


def checkint(num1):
    return num1.isdigit()
import math
number_withdrawal = input("please enter the withdrawal number : ")#enter the number of withdrawal
if(checkint(number_withdrawal)):
    while number_withdrawal >= 1: #using while loop
       if number_withdrawal == 1: #using if condition to check number to win
          print("player1 is the Winner")
          break
       player1 = int(input("Player1 enter a number please: "))
       num_player1 = math.sqrt(player1) #to check if number is perfect spuare
       if player1 <number_withdrawal:  #to chech player enter a number less than number of withdrawal
           if num_player1.is_integer():#to check number is integer
                  number_withdrawal -=player1 #subtract number from withdrawal number
           else:
                  print("Please player1 enter a square number")
                  continue
       else:
         print("please enter a number below 50")
       if number_withdrawal == 1:
         print("player2 is the Winner")
         break
       player2 = int(input("Player2 Enter a number please: "))
       num_player2 = math.sqrt(player2)  #to check if number is perfect spuare
       if player2 <number_withdrawal : #to chech player enter a number less than number of withdrawal
          if num_player2.is_integer():  #to check number is integer
                number_withdrawal -=player2  #substract the number from withdrawal
          else:
              print("Please player2 enter a square number")
              continue
       else:
        print("'please' enter a number below withdrawal")
        continue
else:
    print("invalid")       




