import matplotlib.pyplot as plt

#Graph setup

plt.xlabel('iteration')
plt.ylabel('value')
plt.title('Graph')

#Interaction

print('\n')
start=str(input('    Press Enter to begin ! \n'))

#Variables

init_number = 1 # initial positive number

iterations = int(0) # to count iteration in while loop
List_iteration= [0] # empty list for  iterations ; list to plot
List_number= [0] # empty list for  iterations ; list to plot

#infinity loop

while True: # First while loop

     if (init_number > init_number - 1):# if init number changes or greater then before

         number = init_number # pass value to local varible for calculation


         while True:
             
             if (number%2) == 0: #modulus operator to get the remainder
                  
                 number = int (number/2)    #if number is even make it odd
                 
                 iterations = iterations +1 # Increment
                 
                 List_number.append(number) # Add number/value in list, every time
                 List_iteration.append(iterations) # Add iteration value/increment in list, every time
                 plt.plot(List_iteration, List_number , 'b-o') #Pass variables as arguments to plot, with graph style
  
                 plt.pause(0.0001) #pause for interval seconds
                                   # graph figure, will be updated and displayed before the pause (show data ploting live/animation)
                                  
             else:
                 number = int (number*3+1) #if number is odd make it even
                 
                 
                 iterations = iterations +1 # Increment
                 
                 List_number.append(number) # Add number/value in list, every time
                 List_iteration.append(iterations) # Add iteration value/increment in list, every time
                 plt.plot(List_iteration, List_number, 'b-o') #Pass variables as arguments to plot, with graph style
  
                 plt.pause(0.0001) #pause for interval seconds
                                   # graph figure, will be updated and displayed before the pause (show data ploting live/animation)

                                 
             if (number == 1): # Stop ! jump to next number

                 print('Number : ',init_number)# Current number 
                 print('Iterations : ',iterations, '\n')
                            
                 
                 List_iteration=[0] # reset/empty lists for next round
                 List_number=[0]
                 iterations=int(0)

                 init_number = init_number + 1 #Next number in sequence (by increment of 1)
                 
                 print('Next number : ', init_number, '\n')
  
                 break # exit this loop & go to first while loop
                 
             
            

             
