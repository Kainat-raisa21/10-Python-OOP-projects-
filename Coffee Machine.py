class CoffeeMachine:
    menu_dict = {"espresso":
                    {"water": 200, "milk": 0, "coffee": 75, "price": 150},
                "cappuccino":
                    {"water": 150, "milk": 100, "coffee": 75, "price": 200},
                "latte":
                    {"water": 100, "milk": 150, "coffee": 75, "price": 250}
                }
    stock = {"coffee": 225, "water": 450, "milk": 250}
    public_menu = [["Latte", 250], ["Cappuccino", 200], ["Espresso", 150]]
    account = 0
    orders = []

    def __init__(self):
        pass


    def show_menu(self):
        print("Welcome to Savage Coffee Shop")
        print("Beverege Name")
        for i in range(len(self.public_menu)):
            print(f"{self.public_menu[i][0]}-----{self.public_menu[i][1]} BDT")


    def check_resource(self, drink):
        ans = False
        m = self.menu_dict[drink]
        for item in m:
            if item == "price":
                pass
            elif m[item] <= self.stock[item]:
                ans = True

        return ans


    def take_order(self):
        drink = input("What do you want to order? : ")
        if self.check_resource(drink):
            item = self.menu_dict[drink]
            m = item["price"]
            money = int(input(f"please pay {m}: "))
            self.account += m
            self.orders.append(drink)
            print(f"Your order for a {drink} has succefully been placed")
            return drink
        else:
            return False


    def process_order(self, drink):
        if self.take_order():
            item = self.menu_dict[drink]
            for i in item:
                self.stock -= item[i]

            print(f"your {drink} is ready now!")


if __name__ == "__main__":

    c_maker = CoffeeMachine()

    c_maker.check_resource(c_maker.take_order())
