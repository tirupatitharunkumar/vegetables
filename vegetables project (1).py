 
vegetables=['carrot','potato','onion','tomato','brinjal']
quantity=[50,40,80,100,60]
price=[35,55,50,40,35]
selling_price=[45,65,60,50,25]
revenue=0
total_price=0

customers=[]

cart=[]
quan=[]

while True:
    print( '*'*15,'welcome to sri vinayaka vegetables store','*'*15 )
        
    print('1.owner')
    print('2.customer')
    print('3.exit')

    ch=int(input('Please choose an option to continue: '))
    

    if ch==2:

        customer_name=input('Enter your name: ')
        while True:      
            mobile_number=input('Enter your mobile number: ')

 
            if len(mobile_number)!=10:
                print('Please enter your mobile number correctly...!')

            else:
                break

        customer_details={"name":customer_name,"mobile":mobile_number}
        #print(customer_details)
        if customer_details not in customers:
                customers.append(customer_details)
        #print(customers)

        revenue=0
        total_price=0
        cart1=[]
        qty1=[]
        amount1=[]
        
        
        
        while True:
            #cart1=[]

            #qty=[]
            #amount=[]
                
            print('1.Display Items')
            print('2.Add to cart')
            print('3.View cart')
            print('4.Remove')
            print('5.Modify cart')
            print('6.Bill')
            print('7.Exit')

            

            ch1=int(input('choose an option: '))

            if ch1==1:
                
                print('*'*5,'Items available','*'*5 )
                for i,j,k in zip(vegetables,quantity,selling_price):
                    print('*'*3,i,'-',j,'kgs',k,'Rs','*'*3)
                
            elif ch1==2:
                item=input('Which vegetables do you want to add to the cart: ')

                if item in vegetables:
                    qty=float(input('How many kgs: '))
                    idx=vegetables.index(item)
                    
                    if qty<=quantity[idx]:
                        #print(item,'added to the cart')
                        amount=qty*selling_price[idx]
                        cart1.append(item)
                        qty1.append(qty)
                        amount1.append(amount)

                        #if item not in cart:
                            #cart.append(item)
                            #quan.append(qty)
                        #else:
                           # idx1=cart.index(item)
                           # quan.append(qty)
                            
                        #print('amount: ',amount,'Rs')
                        quantity[idx]=quantity[idx]-qty
                        revenue=revenue+amount
                        total_price=total_price+qty*price[idx]
                        cart.append(item)
                        quan.append(qty)
                        print(f'{item} added to the cart. amount: {amount} Rs')
                        
                    else:
                        print('Out of Stock..!  Available kgs are',quantity[idx])

            elif ch1==3:
                if cart1:
                    print('Items available in your cart are:  ')
                    for m,n,o in zip(cart1,qty1,amount1):
                        print(m,' ',n,'kgs',o,'rs')
                        #print(qty1)
                        #print(amount1)
                    #print(cart1)
                else:
                    print('Your cart is empty..!')


            elif ch1==4:
                item=input('Which item do you want to remove: ')

                if item in cart1:
                    idx1=vegetables.index(item)
                    idx=cart1.index(item)
                    cart1.pop(idx)

                    revenue=revenue-(qty1[idx]*selling_price[idx])
                    total_price=total_price-(qty1[idx]*price[idx1]) 

                    quantity[idx1]=quantity[idx1]+qty1[idx]
                    
                    qty1.pop (idx)
                    amount1.pop(idx)

                    idx2=cart.index(item)
                   
                    quan.pop(idx2)
                    print(item,'item removed successfully')
                
                    #cart1.remove(item)
                    #cart1.remove(qty1)
                    #cart1.remove(amount1)
                else:
                    print(item,'Not existed in cart..!')
                    
            elif ch1==5:
                item=input('Which item do you want to modify: ')
                 
                
                if item in cart1:
                    
                        
                        print('how many kgs do u want to add or remove: ')
                        
                        
                        print('1.add')
                        print('2.remove')
                        
                        ch=int(input('choose an opition: '))
                        
                        
                        if ch==1:
                            
                             
                            new_qty=float(input('how many kgs do u want add: '))
                            #print(new_qty,'kgs','successfully added to the cart')
                            idx=vegetables.index(item)
                            if new_qty>quantity[idx]:
                               print('we are out of stock, avaliable kgs', quantity[idx])
                            else:
                                idx1=cart1.index(item)
                                qty1[idx1]=qty1[idx1]+new_qty
                                quantity[idx]=quantity[idx]-new_qty
                                amount1[idx1]=amount1[idx1]+new_qty*selling_price[idx]
                                revenue=revenue+amount1[idx1]

                                idx2=cart.index(item)
                                quan[idx2]=quan[idx2]+new_qty
                        elif ch==2:
                            new_qty=float(input('how many kgs do u wnat remove: '))
                            #print(new_qty,'kgs','successfully removed from cart')
                            idx=vegetables.index(item)
                            idx1=cart1.index(item)
                            if new_qty>qty1[idx1 ]:
                                print('oops...avaliable kgs in ur cart are: ',qty1[idx1])
                                continue
                                

                            
                            qty1[idx1]=qty1[idx1]-new_qty
                            quantity[idx]=quantity[idx]+new_qty
                            amount1[idx1]=amount1[idx1]-(new_qty*selling_price[idx])
                            revenue=revenue-new_qty*selling_price[idx]

                            idx2=cart.index(item)
                            quan[idx2]=quan[idx2]-new_qty
                        else:
                           print('please select valid option')
                                            
                else:
                    print(item,'Not existed in cart..!')

            elif ch1==6:
                print('*'*10,'BILL','*'*10)
                if cart1:
                    for i,j,k in zip (cart1,qty1,amount1):
                    
                        print('-'*30)
                        print(f'{i}- {j} kgs - {k} Rs')
                        print('-'*30)
                        #print('*'*10,'Thank you for shopping with us','*'*10)
                        #print('  -*-*-*- Have a good day And Visit again  -*-*-*-')
                    #break
                    print('*'*10,'Thank you for shopping with us','*'*10)
                    print('  -*-*-*- Have a good day And Visit again  -*-*-*-')
                    break
                else:
                    print('It Looks like cart is empty,Nothing to bill')


            elif ch1==7:
                print('exiting....!')
                #print('*'*10,'THANK YOU FOR SHOPPING IN OUR STORE','*'*10)
                #print('*'*7,'HAVE A GOOD DAY','*'*7)
                break

            else:
                print('Please choose the valid option....!')



    elif ch==1:
        print('Please login to continue')
        owner_username='tharun'
        owner_password='tharun@21'
        while True:
            username=input('Please enter your username: ')
            
            if username==owner_username:
                password=input('Please enter your password: ')
                if password==owner_password:
                    print('Login successfull')
                    break
                else:
                    print('Password is incorrect')
            else:
                print("username is incorrect")
                print("Please try again")
    

        
        while True:
                
            print('1.Add to inventory')
            print('2.Remove')
            print('3.Update')
            print('4.view')
            print('5.Itemized Profit')
            print('6.Total Profit')
            print('7.Customer details')
            print('8.Exit')

            ch=int(input('Choose an option: '))

            if ch==1:
                item=input('Which vegetable do you want to add : ')
                if item not in vegetables:
                    
                    qty=float(input('Enter quantity of an item: '))
                    cost=int(input('Enter price of an item:'))
                    sell=int(input('Enter selling price of an item:'))
                    vegetables.append(item)
                    quantity.append(qty)
                    price.append(cost)
                    selling_price.append(sell)
                    print('Item is added successfully')
                else:
                    print(item,'is already existed..!')

            elif ch==2:
                item=input('Which vegetable do you want to remove: ')
                if item in vegetables:
                    idx=vegetables.index(item)
                    vegetables.remove(item)
                    price.remove(price[idx])
                    quantity.remove(quantity[idx])
                    
                    print('Item removed successfully')

                else:
                    print(item,'Not existed')

            elif ch==3:
                item=input('Which vegetable do you want to update: ')
                if item in vegetables:
                    idx=vegetables.index(item)
                    qyt=float(input('Enter new quantity: '))
                    pri=int(input('Enter new price: '))
                    sell=int(input('Enter new selling price: '))

                    quantity[idx]=qyt
                    price[idx]=pri
                    selling_price[idx]=sell

                    print(item,'updated successfully..!')
                    

                else:
                    print(item,'not in the inventory..!')

            elif ch==4:
                print('Items in inventory')
                for i,j,k in zip(vegetables,quantity,selling_price):
                    print(i,'-',j,'kgs  -',k,'Rs')

            elif ch==5:
                if  cart:
                         print('itemized_profit: ')

                for i,j in zip(cart,quan):
                            idx=vegetables.index(i)
                            itemized_profit=(j*selling_price[idx]-(j*price[idx]))
                            print(i, '=',itemized_profit, 'RS')
                            
                #pro_item=(input('which item s profit do u want: ' )
                #if pro_item in vegetabes:
                 #       idx=vegetables.index(item)
                          


            elif ch==6:
                profit=revenue-total_price
                if profit>0:
                    print('Total prifit= ',profit,'Rs')
                elif profit<0:
                    print('Total loss= ',profit,'Rs')
                else:
                    print('no loss and no profit')

            elif ch==7:
                #print('Customer details: ')
                if customers :
                    print('\ncustomers details: ')
                    for customer  in customers:
                            print(customer)
                else:
                    print('No details available of customers')

            elif ch==8:
                print('Logged out')
                break
            
            else:
                print('Please choose the valid option')
                

    elif ch==3 :
        print('Exiting...!')
        break

    else:
        print('Please choose the valid option')
        































                
        
