import matplotlib.pyplot as plt

#Graph setup
plt.xlabel('iterations:')
plt.ylabel('value')
plt.title('Graph')

print('\n')
number = int(input(" Pick a number & Press enter 1 2 3 4 5 6 7 8 9... >>>  "))
print('\n')

print('  ',number, ' Good choise ')
print('\n')
print(""" Now we are going to apply two rules.
 If the number is odd, we multiply by three and add one [ x3+1 ]
 If the number is even, we divide by two [ /2 ]
""")
print(' Now we keep applying these two rules.')
print('.')
start=str(input('    Press Enter to begin !'))
print('\n')

List_iteration= [0] # empty list for  iterations ; list to plot

List_number= [0] # empty list for  iterations ; list to plot

iterations = int(0) # to count iteration in while loop

while True:
     
    #infinity loop


     if (number%2) == 0: #modulus operator
         number = int (number/2)    #if number is even make it odd
         print("          ",number)
         iterations = iterations +1 # Increment
         List_number.append(number) # Add number/value in list every time
         List_iteration.append(iterations) # Add Increment in list every time
         plt.plot(List_iteration, List_number) #Pass varibles to plot
         
     else:
         number = int (number*3+1) #if number is odd make it even
         print("          ",number)
         iterations = iterations +1 # Increment
         List_number.append(number) # Add number/value in list every time
         List_iteration.append(iterations) # Add Increment in list every time
         plt.plot(List_iteration, List_number) #Pass varibles to plot
         

     if (number == 1):
         print('\n')
         print(" We are in the loop, and the lowest number in one. Every positive integer, if you apply these rules,")
         print(" will eventually end up in the four, two, one loop. Commonly called Collatz conjecture or 3N+1.")
         print(" And the number you get by applying 3x+1 are called hailstone numbers, beacuse they go up and down like hailstones")
         print('.')
         print('Iterations : ',iterations)
         print('.')
         loopcontinue=str(input('  Press Enter to See the loop ; Close the graph first'))
         print('\n')
         plt.show()
         

