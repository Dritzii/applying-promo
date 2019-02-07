"""
How to apply promotion to a person if they are under a certain age.
Author: John Pham

"""

class shopping():
    def __init__(self,Fname,Lname,Age,Family=None):
        self.firstname = Fname
        self.lastname = Lname
        self.age = Age
        print("Hello {} it is time to add you onto our system :)".format(str(Fname)))
        if Family is None:
            self.family = ''
        elif Family is not None:
            self.family = Family
            print("You have {} people in your family, You may be eligible for a discount :)".format(str(self.family)))
        else:
            print("You are applying with no family members")

    def products(self,items=None):
        self.items = items
        self.cost = self.items * 20
        try:
            print("Checking your products now")
            if items is None:
                print("You have not checked out any items")
                return False
            elif self.age <= 13 and self.family <= 3:
                print("You are eligible for a promo of 20% woo hoo")
                self.cost *= 0.8
                print("Now your cost is ${} yippee".format(str(self.cost)))
                return(self.items)
            elif self.age <= 15 and self.family <= 4:
                print("You have a eligible discount of 50% :)")
                self.cost *= 0.5
                print("Your cost is now ${}".format(str(self.cost)))
                return(self.items)
            else:
                print("You are not allowed a promotion :(, Promotions are only avaliable for families with kids and of a certain age")
                return False
        except:
            print("Error")

        








def main():
    JohnPham = shopping('John','Pham', 15, 3)
    jphamproducts = JohnPham.products(6)





















if __name__ == "__main__":
    main()