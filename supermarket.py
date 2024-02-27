import json


def user_page(cart={}):
    nickname = input('\nEnter your nickname: ')
    print(f'\nWelcome, {nickname}')
    with open('products.json', 'r') as file:
        products = json.load(file)
    is_active = True
    while is_active:
        print('\n1. Search for the product')
        print('2. Add a product to the cart')
        print('3. Edit my cart')
        print('4. See my cart')
        print('5. Proceed payment')
        print('6. Exit')
        action = int(input('\nChoose an option (1, 2, ...): '))
        if action==1:
            product = input('\nEnter product name: ').lower()
            for item, price in products.items():
                if product==item.lower():
                    print(f'Price - {price} KZT')
                    choice = input('Add product to the cart? (yes/no): ').lower()
                    if choice=='yes':
                        quantity = int(input('Quantity: '))
                        cart[item] = quantity
                        with open('cart.json', 'w') as file:
                            json.dump(cart, file)
                        print('\nProduct successfully added to cart')
                        break
                    else:
                        break
                else:
                    print(f'"{product}" do not founded')
                    break
            else:
                '''
                TODO: Реализовать алгоритм поиска похожих продуктов
                Если найдены совпадения - выдать список и дать возможность ввести продукт ещё раз
                Если совпадений нет выдать текущее сообщение 
                '''
                print('\nProduct is out of stock or not found')

        elif action==2:
            product = input('\nEnter product name: ').lower()
            for item, price in products.items():
                if product==item.lower():
                    quantity = int(input('Quantity: '))
                    cart[item] = quantity
                    with open('cart.json', 'w') as file:
                        json.dump(cart, file)
                    print('\nProduct successfully added to cart')
                    break
            else:
                print('\nProduct is out of stock or not found')

        elif action==3:
            cart_action = int(input('\nDelete from cart (0) or change quantity (1)? Enter 0 or 1: '))
            if cart_action==0:
                product = input('\nEnter product name: ').lower()
                for item in cart:
                    if product == item.lower():
                        del cart[item]
                        with open('cart.json', 'w') as file:
                            json.dump(cart, file)
                        print('\nProduct deleted from cart successfully')
                        break
                else:
                    print('\nProduct not found')
            elif cart_action==1:
                product = input('\nEnter product name: ').lower()
                for item in cart:
                    if product == item.lower():
                        new_quantity = int(input('Enter new quantity: '))
                        cart[item] = new_quantity
                        with open('cart.json', 'w') as file:
                            json.dump(cart, file)
                        print('\nCart successfully edited.')
                        break
                else:
                    print('\nProduct not found')
            else:
                print('\nCommand does not exists')

        elif action==4:
            print('\nMy cart:')
            for product, quantity in cart.items():
                print(f'{product} - {quantity}')
        elif action==5:
            _sum = 0
            for item, quantity in cart.items():
                _sum += quantity*products[item]
                print(f'{item} - {quantity} * {products[item]} = {quantity*products[item]} ')
            print('_________________________________')
            print(f'Total = {_sum}')
            print('*********************************')
        elif action==6:
           is_active = False
        else:
            print('\nCommand does not exists')


def admin_page():
    with open('admins.json', 'r') as file:
        data = json.load(file)

    is_active = True
    while is_active:
        login = input('\nEnter login: ').lower()
        password = input('Enter password: ')
        for key, value in data.items():
            if login==key.lower():
                if password==value:
                    login = key
                    is_active = False
                    break
                else:
                    print('\nIncorrect password')
                    break
        else:
            print('\nUser not found')
    print(f'\nWelcome, {login}!')
    is_active = True
    while is_active:
        with open('products.json', 'r') as file:
            products = json.load(file)
        products_copy = products.copy()
        with open('products.json', 'r') as file:
            products = json.load(file)
        print('\n1. Search for the product')
        print('2. Add')
        print('3. Delete')
        print('4. Edit')
        print('5. Change account')
        print('6. Enter as user')
        print('7. Exit')
        action = int(input('\nChoose an option (1, 2, ...): '))
        if action==1:
            product = input('\nEnter product name: ').lower()
            for item, price in products_copy.items():
                if product == item.lower():
                    print(f'Price - {price} KZT')
                    choice = input('What do you want to do? (d-delete/e-edit/c-cancel): ').lower()
                    if choice == 'delete' or choice == 'd':
                        del products[item]
                        with open('products.json', 'w') as file:
                            json.dump(products, file)
                        print('\nProduct successfully deleted from products')
                        break
                    elif choice == 'edit' or choice == 'e':
                        products[item] = int(input('Enter product price: '))
                        with open('products.json', 'w') as file:
                            json.dump(products, file)
                        print('\nProduct successfully edited')
                        break
                    else:
                        break
            else:
                choice = input('Product do not found \n'
                               'Do you want to add this product? (y-yes/n-no): ').lower()
                if choice == 'yes' or choice == 'y':
                    price = int(input(f'Enter price of {product}: '))
                    products[product] = price
                    with open('products.json', 'w') as file:
                        json.dump(products, file)
                    print('\nProduct successfully added to cart')

        elif action==2:
            product = input('\nEnter product name: ').lower()
            for item, price in products_copy.items():
                if product == item.lower():
                    print('This product has already been added to products list')
                    choice = input('What do you want to do? (d-delete/e-edit/c-cancel): ').lower()
                    if choice == 'delete' or choice == 'd':
                        del products[item]
                        with open('products.json', 'w') as file:
                            json.dump(products, file)
                        print('\nProduct successfully deleted from products')
                        break
                    elif choice == 'edit' or choice == 'e':
                        products[item] = int(input('Enter product price: '))
                        with open('products.json', 'w') as file:
                            json.dump(products, file)
                        print('\nProduct successfully edited')
                        break
                    else:
                        break
                else:
                    price = int(input(f'Enter price of {product}: '))
                    products[product] = price
                    with open('products.json', 'w') as file:
                        json.dump(products, file)
                    print('\nProduct successfully added to cart')
                    break

        elif action==3:
            product = input('\nEnter product name: ').lower()
            for item, price in products_copy.items():
                if product == item.lower():
                    del products[item]
                    with open('products.json', 'w') as file:
                        json.dump(products, file)
                    print('\nProduct successfully deleted from products')
                    break
                else:
                    print('This product does not exist')
        elif action==4:
            product = input('\nEnter product name: ').lower()
            for item, price in products_copy.items():
                if product == item.lower():
                    products[item] = int(input('Enter product price: '))
                    with open('products.json', 'w') as file:
                        json.dump(products, file)
                    print('\nProduct successfully edited')
                    break
                else:
                    choice = input('Product do not found \n'
                                   'Do you want to add this product? (y-yes/n-no): ').lower()
                    if choice == 'yes' or choice == 'y':
                        price = int(input(f'Enter price of {product}: '))
                        products[product] = price
                        with open('products.json', 'w') as file:
                            json.dump(products, file)
                        print('\nProduct successfully added to cart')
                    else:
                        break
                    break
        elif action==5:
            is_active = False
            admin_page()
        elif action==6:
            is_active = False
            user_page()
        elif action==7:
            is_active = False
        else:
            print('\nCommand does not exists')


def start_online_supermarket(role):
    if role=='u' or role=='user':
        user_page()
    elif role=='a' or role=='admin':
        admin_page()
    else:
        print('\nRole does not exists\n')
        main()


def main():
    role = input('Choose a role: user (u) or admin (a): ')
    start_online_supermarket(role.lower())


if __name__ == '__main__':
    main()
