"""
How to apply promotion to a person if they are under a certain age- interactive version
Author: John Pham

"""

class shopping():
    def __init__(self):
        self.firstname = input("What is your first name? ")
        self.lastname = input("What is your last name? ")
        self.age = int(input("How old are you? "))
        self.family = input("Do you have family? ")
        if self.family in ['yes','ye','yeah']:
            answer = input("If so how many? ")
            self.count = int(answer)
            if self.count <= 6:
                print("Thanks for letting us know")
            else:
                print("No worries, lets proceed")
        else:
            print("Hello {} it is time to add you onto our system :)".format(str(self.firstname)))

    def products(self):
        items = input("How many items are you buying? ")
        self.items = int(items)
        self.cost = self.items * 20 ## assuming each item is 20 dollars each
        print("Total cost = ${}".format(self.cost))
        print("Checking your products now")
        if self.items is None:
            print("You have not checked out any items")
            return False
        elif self.age >= 25 and self.count <= 1:
            print("You are eligible for a promo of 20% woo hoo")
            self.discount = self.cost * 0.8
            print("Your original cost was ${}".format(str(self.cost)))
            print("Your cost is now ${}".format(str(self.discount)))
            print("You have saved: ${}".format(self.cost - self.discount))
            return(self.items)
        elif self.age <= 15 and self.count <= 20:
            print("You have a eligible discount of 50% :)")
            self.discount = self.cost * 0.5
            print("Your original cost was ${}".format(str(self.cost)))
            print("Your cost is now ${}".format(str(self.discount)))
            print("You have saved: ${}".format(self.cost - self.discount))
            return(self.items)
        elif self.age <= 15 and self.count <= 10:
            print("You have a eligible discount of 60% :)")
            self.discount = self.cost * 0.6
            print("Your original cost was ${}".format(str(self.cost)))
            print("Your cost is now ${}".format(str(self.discount)))
            print("You have saved: ${}".format(self.cost - self.discount))
            return(self.items)
        else:
            print("You are not allowed a discount :(, Promotions are only avaliable for families with kids and of a certain age")
            return(self.cost)
            print(self.cost)
        

        








def main():
    jp = shopping().products()









if __name__ == "__main__":
    main()