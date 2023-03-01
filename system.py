import datetime

#defin class as customer
class customer:

    def InitialDisplay(self):
        heading='''
            Sunway College Bhatbhateni System
                Maitidevi,Kathmandu    '''
        print(heading)

    def initialInformation(self):
        n = int(input("Enter the number of customers: "))
        customer_data = {} #dicti define
        # first for loop for different customers
        for i in range(n):
            customer_data[i] = {}  # nested dic. or multiple dic.
            # input for details
            customer_data[i]['name'] = input(f"Enter the name of customer [{i+1}]: ")
            customer_data[i]['address'] = input(f"Enter the address of customer [{i+1}]: ")
            customer_data[i]['email'] = input(f"Enter the email of customer [{i+1}]: ")
            itemno = int(input(f"Enter the number of items of customer : "))
            customer_data[i]['items'] = {} #dictionary
            customer_data[i]['total'] = 0
            for j in range(itemno):
                itemname = input(f"Enter the name of item [{j+1}]: ")
                itemprice = int(input(f"Enter the price of item [{j+1}]: "))
                itemqty = int(input(f"Enter the quantity of item [{j+1}]: "))
                print("\n")
                customer_data[i]['items'][j] = {'item_name': itemname,'item_price': itemprice, 'item_qty': itemqty, 'total': itemprice*itemqty}
                customer_data[i]['total'] += itemprice*itemqty
        return customer_data


    def calculation(self,customer_data):
        for i in range(len(customer_data)):
            totalPrice = customer_data[i]['total']
            # discount calculation
            discount = 0
            if totalPrice <= 5000:
                discount = totalPrice * 0.05
            elif totalPrice <= 7000:
                discount = (5000 * 0.05) + (totalPrice - 5000) * 0.08
            elif totalPrice <= 10000:
                discount = (5000 * 0.05) + (2000 * 0.08) + (totalPrice - 7000) * 0.10
            else:
                discount = (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (totalPrice - 10000) * 0.15
            # net amount after discount
            netAmount = totalPrice - discount
            customer_data[i]['net_total'] = netAmount
            customer_data[i]['discount'] = discount
        return customer_data

           
    def display_bill(self,customer_data):
        for i in range(len(customer_data)):
            print("Customer Name: ", customer_data[i]['name'])
            print("Customer Address: ", customer_data[i]['address'])
            print("Customer Email: ", customer_data[i]['email'])
            print("\n")
            print("{:<20} {:>10} {:>15} {:>15}".format("Item Name", "Item Price", "Item Quantity", "Total Price"))
            for j in range(len(customer_data[i]['items'])):
                print("{:<20} {:>10} {:>15} {:>15}".format(customer_data[i]['items'][j]['item_name'], customer_data[i]['items'][j]['item_price'], customer_data[i]['items'][j]['item_qty'], customer_data[i]['items'][j]['total']))
            print("\nDiscount: ", customer_data[i]['discount'])
            print("Net Total: ", customer_data[i]['net_total'])
            print("\n")

#customer1 is object of class customer
customer1=customer()
customer1.InitialDisplay()
customer_data=customer1.initialInformation()
customer_data=customer1.calculation(customer_data)
customer1.InitialDisplay()
customer1.display_bill(customer_data)