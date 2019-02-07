"""
How to apply promotion to a person if they are under a certain age.
Author: John Pham

"""

class shopping():
    def __init__(self,Family=None):
        self.firstname = input("What is your first name? ")
        self.lastname = input("What is your last name? ")
        self.age = input("How old are you? ")
        self.family = input("Do you have family? ")
        if self.family in ['yes','ye','yeah']:
            self.family = input("If so how many?" )
        else:
            print("Hello {} it is time to add you onto our system :)".format(str(self.firstname)))

    def products(self,items=None):
        self.items = items
        self.cost = self.items * 20 ## assuming each item is 20 dollars each
        try:
            print("Checking your products now")
            if self.items is None:
                print("You have not checked out any items")
                return False
            elif self.age >= 25 and self.family <= 2:
                print("You are eligible for a promo of 20% woo hoo")
                self.discount = self.cost * 0.8
                print("Your original cost was ${}".format(str(self.cost)))
                print("Your cost is now ${}".format(str(self.discount)))
                print("You have saved: ${}".format(self.cost - self.discount))
                return(self.items)
            elif self.age <= 15 and self.family <= 4:
                print("You have a eligible discount of 50% :)")
                self.discount = self.cost * 0.5
                print("Your original cost was ${}".format(str(self.cost)))
                print("Your cost is now ${}".format(str(self.discount)))
                print("You have saved: ${}".format(self.cost - self.discount))
                return(self.items)
            else:
                print("You are not allowed a discount :(, Promotions are only avaliable for families with kids and of a certain age")
                return(self.cost)
                print(self.cost)
        except:
            print("Error")

        








def main():
    #JohnPham = shopping('John','Pham', 15, 4)
    #jphamproducts = JohnPham.products(6)
    jp = shopping()









if __name__ == "__main__":
    main()