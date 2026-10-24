import datetime
from Lab3 import ArrayQueue

class OrderingSystem:
    def __init__(self):
        self.menu = {"burger": 130, "cheeseburger":150, "fries":75, "soda":25, "sundae":50}
        self.array_queue = ArrayQueue()

    #setter with [order_number, order_items(dict), order_date] as argument 
    def add_order(self, order):
        self.array_queue.enqueue(order)

    #getter for [order_number, order_items(dict), order_date] of front index
    def display_current_order(self):
        order = self.array_queue.front()
        order_num = order[0] 
        order_list = order[1]
        order_date_time = order[2]
        total_price = 0

        #prints out details of order 
        print(f"Order no. {order_num}, {order_date_time} has been completed:")
        #cycles through dict and prints item, quantity, and price
        for menu_item,qty in order_list.items():
            #skips unordered menu items
            if order_list[menu_item] == 0:
                continue
            print(f"{menu_item}: {qty} | {self.menu[menu_item]} each")
            #updates total price while cycling through dict
            total_price += (qty * self.menu[menu_item])
        print(f"Total Price: {total_price}")

    #dequeues order at front index
    def remove_fulfilled_order(self):
        self.array_queue.dequeue()

#MAIN========================
order_system_obj = OrderingSystem()

#UI loop
while True: 
    #represents each order. lists all possible menu items and their ordered qty
    #resets after each iteration
    order = {"burger":0, "cheeseburger": 0, "fries":0, "soda":0, "sundae":0}
    
    answer = input("[1]Add order, [2]Display current order, [3]Remove current: ")
    
    if answer.lower().strip() == "2":
        order_system_obj.display_current_order()
        print()
        continue
    elif answer.lower().strip() == "3":
        order_system_obj.remove_fulfilled_order()
        print()
        continue
    #order loop
    elif answer.lower().strip() == "1":
        print("======== MENU ========")
        print("Burger        Php 130")
        print("Cheeseburger  Php 150")
        print("Fries         Php 75")
        print("Soda          Php 25")
        print("Sundae        Php 50")
        print("======================")

        order_num = int(input("Enter custom receipt number here: "))
        order_date_time = input("Enter date and time of transaction: ")
        
        #outer loop for continuous menu input
        order_validation = True
        while order_validation == True:
            #input validation loop for menu item
            while True:
                order_item = input("Enter menu item here: ") 
                if order_item.lower().strip() not in order:
                    print("Enter a valid menu item")
                    continue
                break
            #input validation loop for quantity
            while True:
                try: 
                    order_qty = int(input(f"Enter qty. of {order_item.lower().strip()}: "))
                    if order_qty <= 0:
                        print("Enter an integer greater than 0")
                        continue
                    break
                except:
                    print("Enter an integer output ")
                    continue
            #input validation for continuous menu input
            while True:
                validation = input("Would you like to add another menu item? (yes/no) ")
                if validation.lower().strip() in ["yes", "no"] and validation == "yes":
                    print("Continuing order...\n")
                    break
                elif validation.lower().strip() in ["yes", "no"] and validation == "no":
                    print("Completing order...\n")
                    #breaks out of outer loop
                    order_validation = False
                    break
                else:
                    print("Enter either yes or no")
                    continue
            #adding input to order dict
            order[order_item.lower().strip()] += order_qty
        #enqueues order after exiting outer loop
        order_system_obj.add_order([order_num, order, order_date_time])
    else:
        print("Enter a valid input (1, 2, or 3)")