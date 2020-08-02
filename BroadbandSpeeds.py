#Broadband Speeds
#Date: 3/02/2016
#Author: Alec Blyth
#Description: This program contains, pseudocode, parameters(find max and min) and asks the user to input thir broadband speed with their postcode

#Varibles 
total = 0
BroadList = []
length = len(BroadList)

#This asks the user for the postcode and save their input 
UserCode = str(input("What is your postcode?"))

#Creating list and inputs
for i in range (0,7):
    newBroadList = int(input("What was your internet speed this week? "))
#Creating input validation to ensure user doesn't input a invalid speed
    while newBroadList < 1 or newBroadList > 72:
        newBroadList = int(input("These speeds are out of limit, enter valid speeds above 0 and below 72"))

    BroadList.append (newBroadList)
#This is sequential file operation, which takes files external of the program like a text file and allows the program to read, edit or delete data.
#This sequential file operation edits the text file 'UserInput.txt' and writes the user's inputs
textFile = open("UserInput.txt", "w")
textFile.writelines(str(BroadList))
textFile.close()

print("")
print(BroadList)
print("")
#Maximum and Minimum Speed algorithm must be placed after input because values don't exist until user input values

def Speeds(BroadList): # This function has the parameter BroadList and finds the max and min speeds 

    maxspeed = BroadList[0]
    minspeed = BroadList[0]
    for i in range (1,7): #This is the pseudocode that performs the maximum and minimum algorithm 
        if BroadList[i] > maxspeed:
            maxspeed = BroadList[i]
            
    for i in range (1,7):
        if BroadList[i] < minspeed:
            minspeed = BroadList[i]

    print("maximum speed is " + str(maxspeed))
    print("")
    print("minimum speed is " + str(minspeed)) 
    print("")

Speeds(BroadList)

#Calculating the averages 
for i in range (0,7):
    total = total + BroadList[i] 

average = total / 7

print("average speed is " + str(average))
print("")
#pseudocode which determine what gets printed out based on average varible 
if average < 11:
    print ("The broadband speed at postcode, " + str(UserCode) + " has been too slow.")
elif average >10 and average <51: 
    print ("The broadband speed at postcode, " + str(UserCode) + " has been reasonably fast.")
elif average > 51:
    print("The broadband speed at postcode. " + str(UserCode) + " has been within the top speed range for your phone line.")   


