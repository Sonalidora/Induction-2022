
import random
print("Enter the target : ", end = "")
target = int(input())
print("Press Enter Key to roll . . . .")
print("~~~~~~~~~~~~~~~~~~~~~~")

sum1 = 0
sum2 = 0
counter = 1
while(True):
    if counter%2 != 0:
        print("player 1 roll  ", end = "")
        k = input()
        K1 = random.randrange(1,7)
        print("player 1 Current toss : ",K1)
        if sum1<target and sum1+K1 <= target:
            sum1 = sum1 + K1
        print(p1,"Total points: ", sum1)
        print("_______________________")
        
    else:
        print("player 2 roll  ", end = "")
        k = input()
        K2 = random.randrange(1,7)
        print("player 2 Current toss :",K2)
        if sum2<target and sum2+K2<= target:
            sum2 = sum2 + K2
        print(p2,"Total points: ", sum2)
        print("______________________")
    
   
    if sum1 == target:
        print("______________________")
        print("Player 1 Wins!")
        print("______________________")
        print("______________________")
        break
   
    elif sum2==target:
        print("_____________________")
        print("Player 2 Wins!")
        print("_____________________")
        print("_____________________")
        break
   
    else:
        counter =counter+1
        continue