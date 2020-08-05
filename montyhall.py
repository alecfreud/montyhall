# -*- coding: utf-8 -*-
import random




stay_wins = 0
switch_wins = 0


simulations = int(input("Enter number of simulations:"))


for i in range(1,simulations): 

    choice = random.randint(1,3)
   

    winner = random.randint(1,3)
 
    
    for i in range (1,4):
        
        if i != choice and i != winner:
            notwinner = i

            break
            
        
    if choice == winner:
        stay_wins += 1

        
    
    for i in range (1,4):
        
        if i != choice and i != notwinner:
            switch = i
          
           
    
    if switch == winner:
        switch_wins +=1
1-100            
print(f"Stay Wins {stay_wins} out of {simulations}")     
print(f"Switch Wins {switch_wins} out of {simulations}")        
   
    
    
    
    
    
    
    

        

    
                 



        
        