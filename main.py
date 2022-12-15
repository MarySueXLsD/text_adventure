R = "\u001b[31m"
G = "\u001b[32m"
W = "\u001b[37m"
Y = "\u001b[33m"
C = "\u001b[36m"

class Shop:
    products = {'apple': 5, 'banana': 7.5, 'coconut': 14.99}

    def add_product(self, name, price):
        self.products[name] = price
        print()

    def delete_product(self, name):
        try:
            del self.products[name]
        except KeyError:
            print('I can\'t find such product')
        print()

    def show_products(self):
        print("Welcome to the shop! We are offering: ")
        for product, price in self.products.items():
            print(f"{product.capitalize()} for ${price}")
        print("Anything you would like to buy?")
        print()


class Player:
    def __init__(self, name):
        self.name = name.capitalize()
        self.cash = 25
        self.products = []
        self.hp = 40

    def add_money(self, extra_cash):
        self.cash += extra_cash

    def spend_money(self, cash):
        self.cash -= cash

    def show_inventory(self):
        print(f"Player {Y}{self.name}{W}:")
        print(f"You have {G}{self.cash}{W} cash on hands")
        if self.products:
            print("Products: ")
        else:
            print("Currently you don't have any products in your inventory")
        for product in self.products:
            print("*" * 5 + " " + Y + product + W + " ", end="*" * 5 + "\n")
        print()

    def buy_product(self, name):
        if name in Shop.products.keys():
            if self.cash > Shop.products[name]:
                self.products.append(name)
                self.cash -= Shop.products[name]
                print(f"You successfully bought {name}")
                return
            print(f"You don't have enough money to buy {name}")
            return
        print(f"We can't find {name}, are you sure you're looking for this?")
        print()


class Work:
    pass

shop = Shop()

print(f"{Y}Stranger:{W} Welcome to the Revalon, stranger!")
print(f"{Y}Stranger:{W} What is your name?")
player = Player(input(f"{Y}You:{W} "))
print(f"{Y}Stan:{W} Oh, nice to meet you {G}{player.name}{W}! My name is Stanley, but everyone calls me {G}Stan{W}")
print(f"{Y}Stan:{W} It's good that you have decided to visit the Center of New-Rouva.")
print(f"{Y}Stan:{W} You can go and buy something, you seem to be very hungry")
print()
print("You see the beautiful center of the city. Decide where will you go")
print(f"{C}Shop{W}, {C}Fountain{W}, {C}Armory{W}, {C}Work{W}")

while True:
    decision = input(f"{Y}{player.name}{W} > ")
    if decision == "inventory" or decision == "inv" or decision == "i":
        player.show_inventory()
    elif decision == "shop" or decision == "buy":
        shop.show_products()
        shop_decision = ""
        while not shop_decision == "exit":
            shop_decision = input(f"{Y}{player.name}{W} > ")
            if shop_decision == "inventory" or shop_decision == "inv" or shop_decision == "i":
                player.show_inventory()
            elif shop_decision == "exit":
                print("You are exiting the shop...")
                print("You see the beautiful center of the city. Decide where will you go")
                print(f"{C}Shop{W}, {C}Fountain{W}, {C}Armory{W}, {C}Work{W}")
                continue
            elif shop_decision in shop.products:
                player.buy_product(shop_decision)




player.buy_product("apple")
player.show_inventory()
player.buy_product("coconut")
player.show_inventory()



