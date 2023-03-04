#Brendan Vick, McKay Boody, Hayden Enloe, Landon Graham, Bryson Lindsey

#Description: Keep a running total of burgers ordered for those in a line of 100.

#A random number of burgers will be assigned to each order.
#Create an Order class that has a method that generates a random amount of burgers
import random
class Order():
        def __init__(self):
                self.burger_count = self.randomBurgers()

        def randomBurgers(self):
                return random.randint(1,20)
        

#Create a Person class that returns a random name through a method called randomName
class Person ():
    def __init__(self):
        self.customer_name = self.randomName ()

    def randomName (self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return asCustomers[random.randint(0,8)]


#Create a Customer subclass that contains an instance variable that is an Order object
class Customer (Person):
      def __init__(self):
        super().__init__()
        self.order = Order()
        

#Main Program
#Create a queue and a dictionary that interact to keep a running total of how many burgers the 9 names ordered out of the 100 orders.
queue_customers = []
dCustomer = {}

iCountQue = 100

#Keep a running total of burgers
for iCount in range (0, iCountQue) :
        oCus = Customer() 
        queue_customers.append(oCus.customer_name)
        if oCus.customer_name in dCustomer :
                dCustomer[oCus.customer_name] += oCus.order.burger_count
        else :
                dCustomer[oCus.customer_name] = oCus.order.burger_count
                
                
#Sort the names in the dictionary from most burgers ordered to least burgers ordered (10,8,4,2, etc.)
listSortedCustomers = sorted(dCustomer.items(), key=lambda x: x[1], reverse=True) 


#Print each customer and their total burgers ordered sorted from most to least ordered
for iCount in range (0,len(listSortedCustomers)) :
    print("\n" + str(listSortedCustomers[iCount]))
