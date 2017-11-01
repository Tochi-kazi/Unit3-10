# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-10
# This program displays average 

print('type in your score')
userinput = input()

counter = 0	
numtotal = 0

for userinput in range (0,100):
    numtotal = numtotal + userinput
    counter = counter + 1
    mark = numtotal / counter
else:
    print(mark)
