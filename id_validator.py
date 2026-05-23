# Title: Automated Security Clearance & Access Control System
# Description: A script that evaluates user IDs and citizen scores to determine 
#              budget allocation, access rights, or trigger security protocols.
# Author: Umar
# Language: Python 3
id = input("put your id")

score = int(input("your score"))

if id == "king":

   print("welcome king your bedget is  dollars")

elif id == "civilian" and score > 5:

    print("you have 10000 dollars you are a good citizen")

elif id == "civilian" and score < 5:

    print("you are a bad citizen only 100 dollars")

else:

    for i in range(100):  

         print("secourity compromized") 

