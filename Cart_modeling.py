class Cart:
    def __init__(self):
        self.items = {}
        self.price_details = {"book":10, "laptop": 30000}
        
    def add_item(self, item_name, quantity): 
        self.items[item_name] = quantity
    def remove_item(self, item_name): 
        del self.items[item_name]
    def update_quantity(self, item_name, updated_quantity):
        self.items[item_name] = updated_quantity
    
    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += quantity * self.price_details[item]
        return total_price
    
    def get_cart_items(self):
        cart_items = []
        for item_name in self.items.keys():
            cart_items.append(item_name)
        return cart_items
        
    
cart_obj = Cart()
cart_obj.add_item("book", 3)
cart_obj.add_item("laptop", 1)
print(cart_obj.items)
print(cart_obj.get_cart_items())
cart_obj.remove_item('laptop')
print(cart_obj.items)
cart_obj.add_item('laptop', 2)
print(cart_obj.items)
cart_obj.update_quantity('book', 5)
print(cart_obj.items)

print(cart_obj.get_total_price())

cart_obj_2 = Cart()
cart_obj_2.add_item("laptop", 1)
print(cart_obj_2.items)
print(cart_obj_2.get_total_price())