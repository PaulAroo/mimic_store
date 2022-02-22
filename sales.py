import listings as ls
price_listing = ls.price_listing
available_items = ls.available_items
item_sub_categories = ls.item_sub_categories


def total_price(quantity, price):
    return quantity * price


def initial():
    print('Here is the list of available items: {}'.format(
        available_items))
    print('Please select one:')
    selected_item = input()
    if selected_item in available_items:
        print('Here are the various types of {} available {}: '.format(
            selected_item, item_sub_categories[selected_item]))
        print('select an item')
        selected_sub_category = input()
        print('The price of {} is ${}'.format(
            selected_sub_category, price_listing[selected_sub_category]))
        print('Select the the qauntity of items you want:')
        quantity = int(input())
        print('The total amount to be paid is: ${}'.format(
            total_price(quantity, price_listing[selected_sub_category])))
    else:
        print(
            "We do not have {}, do you wish to continue shopping? [y/n]".format(selected_item))
        option = input()
        if option == 'y':
            initial()
        else:
            print('BYE FOR NOW')


print('WELCOME TO OUR STORE')
initial()
