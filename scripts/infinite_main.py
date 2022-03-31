import matplotlib.pyplot as plt

#Graph setup

plt.xlabel('iteration')
plt.ylabel('value')
plt.title('Graph')


#Variables

init_number = 1 # initial positive number

iterations = int(0) # to count iteration in while loop
List_iteration= [0] # empty list for  iterations ; list to plot
List_number= [0] # empty list for  iterations ; list to plot

#Interaction
print('\n Do you want to start from a specific number [y/n] ?')
option_number=str(input(' default is 1, enter y or n to continue : '))

if (option_number == 'Y' or option_number == 'y'):
 
    init_number =int(input(' enter the number : '))

print('\n Press Ctrl + C any time to interrupt and to see the plotted graph \n')
start=str(input(' Press Enter to begin ! \n'))

    


try: # for KeyboardInterrupt code section/block

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
                      plt.plot(List_iteration, List_number , 'b-o') #Pass varibles as arguments to plot, with graph style
                   
                  else:
                      number = int (number*3+1) #if number is odd make it even
                      
                      iterations = iterations +1 # Increment
                      
                      List_number.append(number) # Add number/value in list, every time
                      List_iteration.append(iterations) # Add iteration value/increment in list, every time
                      plt.plot(List_iteration, List_number, 'b-o') #Pass varibles as arguments to plot, with graph style
                                      
                  if (number == 1): # Stop ! jump to next number

                      print(' Number : ',init_number, ', Iterations : ',iterations, ', True ', '\n' )#current number values

                      init_number = init_number + 1 #Next number in sequence (by increment of 1)
                      List_iteration=[0] # reset/empty lists for next round
                      List_number=[0]
                      iterations=int(0)

                      break # exit this loop & go to first while loop
                    
                  elif(number == 0): #conjecture break ! (number !=1), if the previous conditions were not true, then try this condition
                       print(' Number : ',init_number, ', Iterations : ',iterations, ', False ', '\n' )#current number values
                       plt.show() # show ploted graph
                       break # exit while loop

               
except KeyboardInterrupt: # if KeyboardInterrupt occur (Ctrl+C by user end programme)
     print(3*'\n', ' Keyboard Interrupt is caught !' , 2*'\n' ,' Please wait, showing graph.....' , 2*'\n')
     plt.show() # show ploted graph
     print('\n', ' exit', 4*'\n')
                        
                 
