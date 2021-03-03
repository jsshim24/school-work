"""
Assignment #8, Part 2
Jun Seob Shim
19/11/2020
Intro to Programming Section 012
Fast Food Restaurant
"""

#product attributes list
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantity = [10, 5, 20]

#set up while loop
notquit = True
while notquit:
    #ask user for which mode
    mode = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")

    #if search mode
    if mode == "s":
        product = input("Enter a product name: ")

        #if the product is in the shop
        if product in product_names:
            position = int(product_names.index(product))
            print("We sell " + '"' + product + '" at ' + str(format(product_costs[position],".2f")) + " per unit")
            print("We currently have " + str(product_quantity[position]) + " in stock")

        #if product isn't in the shop
        else:
            print("Sorry, we don't sell" + ' "' + product + '"')

    #if list mode
    elif mode == "l":
        namelength = 7
        #establish longest name for formatting
        for i in range(len(product_names)):
            if len(product_names[i]) > namelength:
                namelength = len(product_names[i])

        #spacing
        namelength += 4

        pricelength = 5
        #establish longest cost for formatting
        for i in range(len(product_costs)):
            if len(str(product_costs[i])) > pricelength:
                pricelength = len(str(product_costs[i]))

        #spacing
        pricelength += 4

        quantitylength = 8
        #establish longest quantity for formatting
        for i in range(len(product_quantity)):
            if len(str(product_quantity[i])) > quantitylength:
                quantitylength = len(str(product_quantity[i]))
                
        #spacing
        quantitylength += 4

        #print header    
        print(format("Product",f'<{namelength}'),end=" ")
        print(format("Price",f'<{pricelength}'),end=" ")
        print(format("Quantity",f'<{quantitylength}'))

        #print attributes for each product
        for i in range(len(product_names)):
            print(format(product_names[i],f'<{namelength}'),end=" ")
            print(format(product_costs[i],f'<{pricelength}.2f'),end=" ")
            print(format(product_quantity[i],f'<{quantitylength}'))

    #if add mode
    elif mode == "a":
        #set up while loop
        invalidname = True
        
        while invalidname:
            #ask for new product name
            newproduct = input("Enter a new product name: ")

            #if the product is already being sold
            if newproduct in product_names:
                print("Sorry, we already sell that product. Try again.")

            #if the product name is valid
            else:
                invalidname = False

        #set up while loop
        invalidcost = True

        while invalidcost:
            #ask for new product cost
            newcost = float(input("Enter a product cost: "))
            
            #if the cost is valid
            if newcost > 0:
                invalidcost = False

            #if the cost is negative or 0
            else:
                print("Invalid cost. Try again.")

        #set up while loop
        invalidquantity = True

        while invalidquantity:
            #ask for new product quantity
            newquantity = int(input("How many of these products do we have? "))

            #if quantity is valid
            if newquantity > 0:
                invalidquantity = False

            #if quantity is negative or 0
            else:
                print("Invalid quantity. Try again.")

        #add product
        product_names.append(newproduct)
        product_costs.append(newcost)
        product_quantity.append(newquantity)
        print("Product added!")

    #if remove mode
    elif mode == "r":
        #ask which product to remove
        remove = input("Enter a product name: ")

        #if product exists in store
        if remove in product_names:
            #find what index position the specified product is at
            rpos = product_names.index(remove)

            #remove entries at that position from all lists
            del product_names[rpos]
            del product_costs[rpos]
            del product_quantity[rpos]

            #print success
            print("Product removed!")

        #if product doesn't exist in store
        else:
            print("Product doesn't exist. Can't remove.")

    #if update mode
    elif mode == "u":
        #ask which product to update
        update = input("Enter a product name: ")

        #if product exists in store
        if update in product_names:
            #find index position of product in lists
            upos = product_names.index(update)
            
            print("What would you like to update?")

            #set up while loop
            invalidupdate = True

            while invalidupdate:            
                updatemode = input("(n)ame, (c)ost or (q)uantity: ")

                #if updating name
                if updatemode == "n":
                    invalidupdate = False

                    #set up while loop
                    duplicatename = True

                    while duplicatename:
                        #ask for new name
                        newname = input("Enter a new name: ")

                        #if name is a duplicate
                        if newname in product_names:
                            print("Duplicate name!")

                        #if new name is valid
                        else:
                            #update name in product names list
                            product_names[upos] = newname

                            #print success
                            print("Product name has been updated")
                            duplicatename = False

                #if updating cost
                elif updatemode == "c":
                    invalidupdate = False

                    #set up while loop
                    invalidnewcost = True

                    while invalidnewcost:
                        newcost = float(input("Enter a new cost: "))

                        #if cost is valid
                        if newcost > 0:
                            invalidnewcost = False

                            #update cost in product costs list
                            product_costs[upos] = newcost

                            #print success
                            print("Product cost has been updated")
                                                       
                        #if cost is invalid
                        else:
                            print("Invalid cost!")

                elif updatemode == "q":
                    invalidupdate = False

                    #set up while loop
                    invalidnewquantity = True

                    while invalidnewquantity:
                        newquantity = int(input("Enter a new quantity: "))

                        if newquantity > 0:
                            invalidnewquantity = False

                            #update quantity in product costs list
                            product_quantity[upos] = newquantity

                            #print success
                            print("Product quantity has been updated")

                        #if cost is invalid
                        else:
                            print("Invalid quantity!")

                else:
                    print("Invalid option")

        #if product doesn't exist in store
        else:
            print("Product doesn't exist. Can't update.")

    #if report mode
    elif mode == "e":
        #print most expensive
        print(format("Most expensive product:","29s"),end="")
        print(max(product_costs)," (",product_names[product_costs.index(max(product_costs))],")",sep="")

        #print least expensive
        print(format("Lest expensive product:","29s"),end="")
        print(min(product_costs)," (",product_names[product_costs.index(min(product_costs))],")",sep="")

        #calculate total inventory cost
        totalcost = 0
        for c in range(len(product_costs)):
            totalcost += product_costs[c]*product_quantity[c]

        #print totalcost
        print(format("Total value of all products:","29s"),end="")
        print(round(totalcost,2))

    #if quit mode, quit and stop running while loop
    elif mode == "q":
        print("See you soon!")
        notquit = False

    #if not a valid mode
    else:
        print("Invalid option, try again")

    #spacing
    print()

