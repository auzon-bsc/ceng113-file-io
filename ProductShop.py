#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:23:25 2018

@author: oguzhan
"""
#-----FILE READING-----

filePurchaseHistory = open("PurchaseHistory.txt", "r")
purchaseHistory = filePurchaseHistory.readlines()
filePurchaseHistory.close()
cleanPurchaseHistory = []

filePriceList = open("PriceList.txt", "r")
priceList = filePriceList.readlines()
filePriceList.close()
lenghtPriceList = int(len(priceList))
cleanPriceList = []

#-----CLEAN -----

for i in priceList:
    nameNprice = []
    price = ""
    name = ""

    for j in i:
        try:
            j = int(j)
            digit = str(j)
        except:
            continue
            
        price += digit
    
    for k in i:
        if k.isalpha() == True or k.isspace() == True:
            name = name + k
    name = name.strip()        
    nameNprice.append(name)
    nameNprice.append(price)
    cleanPriceList.append(nameNprice)
    

#-----THIS BLOCK FOR GETTING BETTER CLEAN LIST FOR STUDY-----

e = []

for line in purchaseHistory:
    a = line.split("-")
    b = ",".join(a)
    c = b.split(",")
    
    for i in range(int(len(c))):
        d = c[i].strip()
        e.append(d)

#-----THIS BLOCK IS FOR DAY and STUDENT SIZE-----

counterStudent = -1
counterDay = -1
listID = []

for i in e:
    forkLift = 0
    checkDay = i[forkLift:forkLift + 3]
    checkStudent = i[forkLift:forkLift + 7]

    if checkDay == "DAY": 
        counterDay += 1
        cleanPurchaseHistory.append([])
    
    elif checkStudent == "STUDENT":
        studentID = i.strip("STUDENT")
        listID.append(studentID)
        
for i in range(counterDay+1):
    studentNumber = int(max(listID))
    for j in range(studentNumber+1):
        cleanPurchaseHistory[i].append([])

inNum = 0
for i in e:
    checkDay = i[forkLift:forkLift + 3]
    checkStudent = i[forkLift:forkLift + 7]

    if checkDay == "DAY":
        dayNumber = i.strip("DAY#")
        dayNumber = int(dayNumber)
        
    elif checkStudent == "STUDENT":
        studentID = i.strip("STUDENT")
        studentID = int(studentID)
        inNum = 0
        
            
    else:
        cleanPurchaseHistory[dayNumber-1][studentID-1].append(i)
        inNum += 1
         
#-----MENU-----

choice = -1
    
while choice != 0:
    print("Press 1 to product and price list\n" 
          "Press 2 to total revenue and most selling product(s) in total\n"
          "Press 3 to total revenue and most selling product(s) in a day\n"
          "Press 4 to total payment for a student\n"
          "Press 0 to exit")
    
    choice = input("Your choice: ")
    choice = int(choice)
    
#-----CHOICE == 1-----#
    
    if choice == 1:
        print("PRODUCT           PRICE\n")
        
        
        for i in cleanPriceList:
            indentationNumber = 20 - int(len(i[0]))
            indentation = " " * indentationNumber
            print(i[0] + indentation + i[1])

#-----CHOICE == 2 -----#

    elif choice == 2:
        totalrevenue = 0
        mostSaleList = [[], []]
        
        for duo in cleanPriceList:
                        
            for day in cleanPurchaseHistory:
                
                for student in day:            
                    
                    for sale in student:
                        
                        if duo[0] == sale:
                            totalrevenue += int(duo[1])
            
            mostSaleList[0].append(duo[0])
            mostSaleList[1].append(e.count(duo[0]))
        
        print("\nTotal revenue:", totalrevenue)

        mostSaleProductCount = max(mostSaleList[1])
        
        print("\nMost selling product(s) in TOTAL (", mostSaleProductCount, 
              "sales )\n")
        
        for i in range(int(len(mostSaleList[1]))):
            
            if mostSaleList[1][i] == mostSaleProductCount:
                print(mostSaleList[0][i])

#-----CHOICE == 3 -----#

    elif choice == 3:
        promt = "Select day between 1 and " + str(dayNumber) + ": "
        dayChoice = input(promt)
        dayChoice = int(dayChoice)
        lst = []
        maxRep = 0
        dailyRevenue = 0
        
        for duo in cleanPriceList:
            
            for student in cleanPurchaseHistory[dayChoice - 1]:
            
                for sale in student:
                    
                    if sale == duo[0]:
                        dailyRevenue += int(duo[1])
                        lst.append(sale)

            temp = lst.count(duo[0])
            
            if temp > maxRep:
                maxRep = int(temp)
        
        print("Daily revenue: ", dailyRevenue)
        
        for i in range(int(len(lst)) - maxRep + 1):
            if lst[i] == lst[i + maxRep - 1]:
                print(lst[i])
                
#-----CHOICE == 4 ----#
                
    elif choice == 4:
        promt = "Select ID between 1 and " + str(studentNumber) + ": "
        choiceStudent = int(input(promt))
        total = 0
        choiceStudent -= 1
        
        for duo in cleanPriceList:
        
            for day in cleanPurchaseHistory:
                    
                for sale in day[choiceStudent]:
                
                    if duo[0] == sale:
                            
                        total += int(duo[1])
    
        print("\nTotal payment of the student: ", total, "\n")            