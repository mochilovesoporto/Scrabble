class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        return self.name + " is available from " + str(self.start_time) + " to " + str(self.end_time)
    def calculate_bill(self, purchased_items):
        bill = 0
        for key, value in purchased_items.items():
            if key in self.items:
                bill += value
        return bill
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    def __repr__(self):
        return self.name

# Menu & Franchise Class Menus & Objects
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu("Brunch", brunch_items, 1100, 1600)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                    'coffee': 1.50, 'espresso': 3.00}

early_bird = Menu("Early Bird Dinner", early_bird_items, 1500, 1800)

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids = Menu("Kids", kids_items, 1100, 2100)

# Business class Menu and Object
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas = Menu("Arepas menu", arepas_items, 1000, 2000)

# Main()

# Use Menu class Method to calculate cost of purchase from specific menu
print(brunch.calculate_bill({'pancakes': 7.50, 'home fries': 4.50, 'coffee': 1.50}))

print(early_bird.calculate_bill({'salumeria plate': 8.00, 'mushroom ravioli (vegan)': 13.50}))

# Flagship class object creation
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)

# Print available menus at Flagship business
print(flagship_store.available_menus(1100))

# Franchise creation for Business class
arepas_place = Franchise("189 Fitzerald Avenu", arepas)

# Flagship object instantiation
Business("Basta Fazoolin' with my heart", [flagship_store, new_installment])

Business("Take a' Arepa", arepas_place)
