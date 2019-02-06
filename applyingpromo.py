"""
How to apply promotion to a person if they are under a certain age.
Author: John Pham

"""

class person(object):
    def __init__(self,Fname,Lname,Age,Cost,Family=None):
        self.firstname = Fname
        self.lastname = Lname
        self.age = Age
        self.cost = Cost
        print("Hello {} it is time to add you onto our system :)".format(str(Fname)))
        if Family is None:
            self.family = ''
        else:
            self.family = Family
            print("You have {} people in your family :)".format(str(self.family)))
        if Age <= 13 and Family is not None:
            print("You are eligible for a promo of 50% woo hoo because you are under 13 :)")
            self.cost *= 0.5
            print("Now your cost is ${} yippee".format(str(self.cost)))
        elif Age <= 15 and Family <= 4:
            print("You have a eligible discount of 20% :)")
            self.cost *= 0.8
            print("Your cost is now ${}".format(str(self.cost)))
        else:
            print("You are not allowed a promotion :(, Promotions are only avaliable for families with kids")


    

        










def main():
    JohnPham = person('John','Pham', 15, 50, 3)











if __name__ == "__main__":
    main()