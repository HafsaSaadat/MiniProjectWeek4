# ''' Mini Project week4'''

from ast import Break
from itertools import product
from pickle import FALSE, TRUE
from turtle import clear
from functions_projects import add_Item_List,add_courier_info,del_Item_List,update_courier_infoc
import csv


def display_Main_Menu():
    str_Mesg = """ ***********Welcome to Gourmet Cafe***********
    ***********Main Menu***********
    Please choose one of the following options : 
    0 -- exit || 1 -- Product Menu || 2 -- Order Menu || 3 -- Courier Menu 
    """
    print(str_Mesg)


def display_Product_Menu():
    str_Product_Mesg = """\t***********Product Menu***********
    Please choose one of the following options: 
    5 --Retrun to main menu ||6 --View Products||2 --Add new Product||3 -- Update Product||4--Delete Product 
    """
    print(str_Product_Mesg)


def display_Order_Menu():
    str_Order_Mesg = """\t***********Order Menu***********
    Please choose one of the following options: 
    7 --Retrun to main menu ||8 --View Order||9 --Place Order
    10 --Update Order status List||11--Update Order||12--Delete Order 
    """
    print(str_Order_Mesg)


def display_Courier_Menu():
    str_Courier_Mesg = """\t***********Courier Menu***********
    Please choose one of the following options: 
    13 --Retrun to main menu ||14 --View Courier List||15 --Add New Courier
    16 -- Update Existing Courier||17--Delete Existing Courier  
    """
    print(str_Courier_Mesg)


def print_Item_List(item_list):
    indent = 2
    for i in range(len(item_list)):
        print(' ' * indent, 'Index ', i, ':', item_list[i])


# def add_Item_List(str_item, str_item_price, exiting_list):
#     exiting_list.append({"name": str_item, "price": str_item_price})
#     return exiting_list


# def del_Item_List(item_index, exiting_list=[]):
#     exiting_list.pop(item_index)
#     return exiting_list


def update_Item_List(item_index, item, item_price, exiting_list=[]):
    exiting_list[item_index]["name"] = item
    exiting_list[item_index]["price"] = item_price
    return exiting_list


def del_Order_Dict_List(item_index, exiting_list=[]):
    exiting_list.pop(item_index)
    return exiting_list


def print_order_status_List(order_status_list):
    indent = 2
    for i in range(len(order_status_list)):
        print(' ' * indent, 'Index ', i, ':', order_status_list[i])


def print_Courier_List(courier_list):
    indent = 2
    for i in range(len(courier_list)):
        print(' ' * indent, 'Index ', i, ':', courier_list[i])

# print Available orders List


def print_cutomer_order_List(order_dict_list):
    indent = 2
    for i in range(len(order_dict_list)):
        print(' ' * indent, 'Index ', i, ':', order_dict_list[i],'\n')


# def add_courier_info(str_courier_name, str_courier_phone, exiting_list):
#     exiting_list.append({"name": str_courier_name, "phone": str_courier_phone})
#     return exiting_list


# def update_courier_info(courier_index, courier_name, courier_ph, exiting_list=[]):
#     exiting_list[courier_index]["name"] = courier_name
#     exiting_list[courier_index]["phone"] = courier_ph
#     return exiting_list


def Load_Product_List():
    file = None
    try:
        product_list = []
        file = open('products.csv', 'r')
        reader = csv.DictReader(file)
        product_list = list(reader)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return product_list
    finally:
        file.close()
        return product_list


def dump_Product_List_File(product_list):
    file = None
    try:
        file = open('products.csv', 'w')
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(product_list)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        file.close()


def Load_Courier_List():
    file = None
    try:
        courier_list = []
        # file = open("courier.txt", "r")
        file = open("courier.csv", "r")
        # lines = file.readlines()
        # for line in lines:
        #     courier_list.append(line.strip())
        reader = csv.DictReader(file)
        courier_list = list(reader)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return courier_list
    finally:
        file.close()
        return courier_list


def dump_Courier_List_File(courier_list):
    file = None
    try:
        # file = open("courier.txt", "w")
        # for i in range(len(courier_list)):
        #     file.write(courier_list[i]+"\n")
        file = open('courier.csv', 'w')
        writer = csv.DictWriter(file, fieldnames=['name', 'phone'])
        writer.writeheader()
        writer.writerows(courier_list)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        file.close()

# Read all customer orders from csv file


def Load_orders_list():
    file = None
    try:
        orders_list = []
        file = open('orders.csv', 'r')
        reader = csv.DictReader(file)
        orders_list = list(reader)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return orders_list
    finally:
        file.close()
        return orders_list


def dump_Orders_list(order_list):
    file = None
    try:
        file = open('orders.csv', 'w')
        writer = csv.DictWriter(file, fieldnames=[
                                'customer_name', 'customer_address', 'customer_phone', 'customer_courier', 'status', 'items'])
        writer.writeheader()
        writer.writerows(order_list)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        file.close()


# product_list = ["Coke Zero","Coke Regular","Orange Juice","Apple Juice"]
product_list = Load_Product_List()
# order_Dict = [{"customer_name":"Joe","customer_address": "Preston","customer_phone": "0213685","customer_courier":0,"status": "Delivered","items":"0,1,2"}]
order_Dict = Load_orders_list()
order_status_list = ["Preparing", "Awaiting Pickup",
                     "Out-for-Delivery", "Delivered"]
courier_list = Load_Courier_List()
bMainFlag = True

while bMainFlag:
    display_Main_Menu()
    main_menu_inp = int(input())

    if (main_menu_inp == 0):
        print("Thanks for visiting the store, See you Again")
        dump_Product_List_File(product_list)
        dump_Courier_List_File(courier_list)
        dump_Orders_list(order_Dict)
        bMainFlag = FALSE
        break
        # exit

    elif(main_menu_inp == 1):
        # display_sub_Menu()
        # sub_menu_inp = int(input())

        while True:
            display_Product_Menu()
            sub_menu_inp = int(input())

            if (sub_menu_inp == 5):
                bMainFlag = TRUE
                break

            elif (sub_menu_inp == 6):
                print("Available List of product:")
                print_Item_List(product_list)

            elif(sub_menu_inp == 2):
                append_product_item = str(
                    input("Enter product name to add in List:"))
                append_product_price = str(input("Product price to: "))
                print(add_Item_List(append_product_item,
                      append_product_price, product_list))

            elif(sub_menu_inp == 3):

                print("Available product List is:")
                print_Item_List(product_list)
                index_update = int(
                    input("Enter index of a product you want to update"))

                product_update = input(
                    "Enter the product name you want to add: ")
                if product_update == "":
                    product_update = product_list[index_update]["name"]

                product_price = input("Enter the price you want to update: ")
                if product_list == "":
                    product_price = product_list[index_update]["price"]
                print("updated List", update_Item_List(index_update,
                      product_update, product_price, product_list))

            elif(sub_menu_inp == 4):

                # print("Existing Product List")
                # for i in range(len(product_list)):
                #     print(i,product_list[i])

                print("Available product List is:")
                print_Item_List(product_list)
                index_delete = int(
                    input("Enter the index where you want to delete product : "))
                print("updated List after deletion",
                      del_Item_List(index_delete, product_list))
            else:
                print("Incorrect selection")

    elif(main_menu_inp == 2):
        display_Order_Menu()
        order_menu_input = int(input())

        if (order_menu_input == 7):
            bMainFlag = TRUE

        elif (order_menu_input == 8):
            print("*** Available Order List***")
            print_cutomer_order_List(order_Dict)

        elif (order_menu_input == 9):

            cust_name = input("Please Enter your name: ")
            cust_add = input("Please enter your address: ")
            cust_phone = input("Enter phone number: ")

            print("Available courier List")
            print_Courier_List(courier_list)
            # check for incorrect input
            cust_courier = input(
                "Please select index number of the item for your order:")

            # while placing order the status is always set to prepraring
            cust_order_status = order_status_list[0]

            # Display available product
            # ask for index number of product user wishes to add in order
            str_order_index = ""
            temp = []
            while True:
                # Display Avaibale products to choose for order
                print_Item_List(product_list)
                order_index = int(
                    input("Enter the index of product you would like to add: "))
                temp.append(order_index)
                str_continue = str(
                    input("Would you like to add another item(y/n)?")).lower()
                if str_continue == 'y':
                    continue
                else:
                    break
            # converting order list into string variable followed by join
            order_product_index = (', '.join(str(x) for x in temp))

            order_Dict.append({"customer_name": cust_name, "customer_address": cust_add, "customer_phone": cust_phone,
                              "customer_courier": cust_courier, "status": cust_order_status, "items": order_product_index})
            print("Your Order is on the way!")

        elif (order_menu_input == 10):

            print("List of existing order status List")
            print_order_status_List(order_status_list)
            index_order_status = int(
                input("Enter the index you want to update order status"))
            if 0 <= index_order_status < len(order_status_list):
                print()
            else:
                print("Index doesn't exist in the List")
                break
            order_status = input("Enter the status you want to update: ")
            order_status_list[index_order_status] = order_status
            print("updated Order status List")
            print_order_status_List(order_status_list)

        elif (order_menu_input == 11):
            print("Displaying Available Orders")
            print_cutomer_order_List(order_Dict)
            index_order_update = int(
                input("Enter the index of order you to update:"))
            # if index doesnt exitst the application breaks
            if 0 <= index_order_update < len(order_Dict):
                print()
            else:
                print("Index doesn't exist in the List")
                break

            cust_name = input(
                "Please the name you want to update or press enter to leave it unchanged")
            if cust_name != "":
                order_Dict[index_order_update]["customer_name"] = cust_name

            cust_add = input(
                "Please enter your address to update or press enter to leave it unchanged")
            if cust_add != "":
                order_Dict[index_order_update]["customer_address"] = cust_add

            cust_phone = input(
                "Enter phone number to update or press enter to leave it unchanged")
            if cust_phone != "":
                order_Dict[index_order_update]["customer_phone"] = cust_phone

            cust_courier = input(
                "Enter index of courier to update or press enter to leave it unchanged")
            if cust_courier != "":
                order_Dict[index_order_update]["customer_courier"] = cust_courier

            print("List of items in current order is: ",
                  order_Dict[index_order_update]["items"])
            cust_order_old_item = input(
                "Enter index of item you want to change or press enter to leave it unchanged")
            print("Avaibale items in cafe is:")
            print_Item_List(product_list)
            cust_order_new_item = input(
                "Enter index of item you want to add or press enter to leave it unchanged")
            txt = str(order_Dict[index_order_update]["items"])
            if cust_order_old_item != "" and cust_order_new_item != "":
                str_neworder = txt.replace(
                    str(cust_order_old_item), str(cust_order_new_item))
            order_Dict[index_order_update]["items"] = str_neworder

            indent = 2
            print(' ' * indent, 'Index ', index_order_update,
                  ':', order_Dict[index_order_update])

        elif(order_menu_input == 12):
            indent = 2
            for i in range(len(order_Dict)):
                print(' ' * indent, 'Index ', i, ':', order_Dict[i], '\n')

            index_del = int(
                input("Enter the index of order you want to delete: "))
            order_Dict = del_Item_List(index_del, order_Dict)
            if len(order_Dict) == 0:
                print("No more order in List")
            else:
                print("updated Order List", order_Dict)
    elif(main_menu_inp == 3):

        display_Courier_Menu()
        courier_menu_input = int(input())
        if (courier_menu_input == 13):
            bMainFlag = TRUE

        elif (courier_menu_input == 14):
            print_Courier_List(courier_list)

        elif (courier_menu_input == 15):
            courier_name = input(
                "Enter the courier name you want to add in List")
            courier_phone = input("Enter the courier phone# you want to add:")
            print("Updated Courier List")
            print_Courier_List(add_courier_info(
                courier_name, courier_phone, courier_list))

        elif (courier_menu_input == 16):
            print("Update Courier information in List")
            print_Courier_List(courier_list)
            index_update = int(
                input("Enter the index where you want to update courier info:"))

            courier_name = input("Enter the name you want to update")
            if courier_name == "":
                courier_name = courier_list[index_update]["name"]

            courier_phone = input("Enter the courier phone# you want to add:")
            if courier_phone == "":
                courier_phone = courier_list[index_update]["phone"]
            print("updated Courier List", update_courier_info(
                index_update, courier_name, courier_phone, courier_list))

        elif (courier_menu_input == 17):
            print("Available courier List")
            print_Courier_List(courier_list)
            index_del = int(
                input("Enter the index of order you want to delete: "))
            if 0 <= index_del < len(courier_list):
                print()
            else:
                print("Index doesn't exist in the List")
                bMainFlag = TRUE
                break

            courier_list = del_Item_List(index_del, courier_list)
            if len(courier_list) == 0:
                print("No more courier providers in List")
            else:
                print("updated Courier List", courier_list)
        # else:
        #     print("Incorrect selection")
    else:
        print("Incorrect selection")
        # Print_Main_Menu()
        # main_menu_inp = int(input())
