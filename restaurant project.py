import pymysql


con = pymysql.connect(
    user='root',
    password='tharun@21',
    host='localhost',
    database='project1'
)
cur = con.cursor()


menu = [
    [1, 'Veg Biryani', 320, 'Main Course'],
    [2, 'Chicken Biryani', 480, 'Main Course'],
    [3, 'Paneer Butter Masala', 350, 'Main Course'],
    [4, 'Butter Naan', 90, 'Main Course'],
    [5, 'Chicken 65', 360, 'Starter'],
    [6, 'Masala Dosa', 160, 'Breakfast'],
    [7, 'Idli Sambhar', 140, 'Breakfast'],
    [8, 'Gobi Manchurian', 300, 'Starter'],
    [9, 'Egg Curry', 310, 'Main Course'],
    [10, 'Mineral Water', 250, 'Beverage'],
    [11, 'Lobster Thermidor', 1950, 'Main Course'],
    [12, 'Truffle Mushroom Risotto', 1600, 'Main Course'],
    [13, 'Grilled Norwegian Salmon', 1850, 'Main Course'],
    [14, 'Lamb Chops with Red Wine Jus', 1780, 'Main Course'],
    [15, 'Prawn Malai Curry', 1720, 'Main Course'],
    [16, 'Chicken Cordon Bleu', 1670, 'Main Course'],
    [17, 'Stuffed Bell Peppers', 1350, 'Main Course'],
    [18, 'Tandoori Pomfret', 1700, 'Starter'],
    [19, 'Veg Thai Green Curry & Rice', 1500, 'Main Course'],
    [20, 'Chocolate Lava Cake', 550, 'Dessert']
]

orders = []
day_wise_profit = 0


cur.executemany('''
    INSERT IGNORE INTO elite1 (sno, item, price, category)
    VALUES (%s, %s, %s, %s)
''', menu)
con.commit()



while True:
    print(10 * '*', 'Welcome to the Elite Star Restaurant', 10 * '*')
    print('1. Admin')
    print('2. User')
    print('3. Exit')

    ch = input('Choose one option: ')

    
    if ch == '1':
        ido, pd = '1', '1'
        op = input('Enter your ID: ')
        if op == ido:
            pwd = input('Enter your password: ')
            if pwd == pd:
                print('✅ Logged in successfully!')
                while True:
                    print('\n--- Admin Menu ---')
                    print('1. View Menu')
                    print('2. Add Item')
                    print('3. Modify Menu')
                    print('4. View All Orders')
                    print('5. Day Wise Profit')
                    print('6. Exit')
                    ch = input('Select option: ')

                    if ch == '1':
                        for i in menu:
                            print('*' * 5, i, '*' * 5)

                    elif ch == '2':
                        sno = int(input('Enter serial number: '))
                        item = input('Enter item name: ')
                        price = int(input('Enter price: '))
                        category = input('Enter category: ')
                        menu.append([sno, item, price, category])
                        cur.execute(
                            'INSERT INTO elite1(sno,item,price,category) VALUES (%s,%s,%s,%s)',
                            (sno, item, price, category)
                        )
                        con.commit()
                        print('✅ Item successfully added!')

                    elif ch == '3':
                        print('1. Update Price')
                        print('2. Delete Item')
                        ch2 = input('Choose option: ')

                        if ch2 == '1':
                            up = input('Enter item name to update: ').strip().lower()
                            found = False
                            for k in menu:
                                if up == k[1].lower():
                                    new_price = int(input('Enter new price: '))
                                    k[2] = new_price
                                    cur.execute(
                                        'UPDATE elite1 SET price=%s WHERE item=%s',
                                        (new_price, k[1])
                                    )
                                    con.commit()
                                    print('✅ Price updated!')
                                    found = True
                                    break
                            if not found:
                                print('❌ Item not found!')

                        elif ch2 == '2':
                            delt = input('Enter item name to delete: ').strip().lower()
                            found = False
                            for j in menu:
                                if delt == j[1].lower():
                                    confirm = input('Are you sure? (yes/no): ').lower()
                                    if confirm == 'yes':
                                        menu.remove(j)
                                        cur.execute(
                                            'DELETE FROM elite1 WHERE item=%s',
                                            (j[1],)
                                        )
                                        con.commit()
                                        print('✅ Item removed!')
                                    found = True
                                    break
                            if not found:
                                print('❌ Item not found!')

                    elif ch == '4':
                        if orders:
                            for i in orders:
                                print(i)
                        else:
                            print('No orders placed yet.')

                    elif ch == '5':
                        print("Today's Profit: ₹", day_wise_profit)

                    elif ch == '6':
                        print('Exiting admin...')
                        break

                    else:
                        print('Invalid option.')

            else:
                print('❌ Incorrect password.')
        else:
            print('❌ Incorrect ID.')


    elif ch == '2':
        print(5 * '*', 'Welcome User', 5 * '*')
        name = input('Enter your name: ')

        try:
            mobile = int(input('Enter mobile number: '))
            if len(str(mobile)) == 10:
                print('✅ Login successful!')
                cur.execute(
                    'INSERT INTO customer1(cname, cmobile) VALUES (%s, %s)',
                    (name, mobile)
                )
                con.commit()
                cart = []
                while True:
                    print('\n--- User Menu ---')
                    print('1. View Menu')
                    print('2. Modify Cart')
                    print('3. View Cart')
                    print('4. Bill')
                    print('5. Exit')
                    ch3 = input('Choose option: ')

                    if ch3 == '1':
                        for i in menu:
                            print('*' * 5, i, '*' * 5)

                    elif ch3 == '2':
                        mod = input('Do you want to add/remove? ').lower()
                        if mod == 'add':
                            add = input('Enter item name: ')
                            for item in menu:
                                if add.lower() == item[1].lower():
                                    cart.append(item)
                                    orders.append([item[1], item[2], 'by', name])
                                    day_wise_profit += item[2]
                                    cur.execute(
                                        'UPDATE customer1 SET orders=%s WHERE cmobile=%s',
                                        (add, mobile)
                                    )
                                    con.commit()
                                    print('✅ Item added to cart!')
                                    break
                            else:
                                print('❌ Item not available.')

                        elif mod == 'remove':
                            rem = input('Enter item name: ')
                            for c in cart:
                                if rem.lower() == c[1].lower():
                                    cart.remove(c)
                                    print('✅ Item removed from cart!')
                                    break
                            else:
                                print('❌ Item not in cart.')

                    elif ch3 == '3':
                        print(f"{name}'s Cart:")
                        if cart:
                            for i in cart:
                                print(i)
                        else:
                            print('Cart is empty.')

                    elif ch3 == '4':
                        if cart:
                            print('--- Bill ---')
                            total = 0
                            for i in cart:
                                print(i[1], ":", i[2])
                                total += i[2]
                            print("Total Bill: ₹", total)
                        else:
                            print('Cart is empty.')

                    elif ch3 == '5':
                        print('Exiting user menu...')
                        break

                    else:
                        print('Invalid option.')
            else:
                print('❌ Invalid mobile number.')
        except ValueError:
            print('❌ Digits only for mobile number!')

    elif ch == '3':
        print('🙏 Thank you for visiting!')
        break
    else:
        print('❌ Invalid option.')


con.commit()
cur.close()
con.close()
