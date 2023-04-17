class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price
        
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Rating: {}".format(self.rating))
        
    def get_deal_price(self):
        return self.deal_price
        
class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months
    def get_warranty(self):
        return self.warranty_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty_in_months))

class GroceryItem(Product):
    def __init__(self,name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
    
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))

class Order:
    delivery_charges = {"prime_members": 0, "non_prime_members": 50 }
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
    
    def add_item(self, product, quantity):
        self.items_in_cart.append((product,quantity))
        
    def display_order_details(self):
        print("-----------Products in Cart------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()       #modeling instances of one class `ElectronicItem` or `GroceryItem` as attributes of another class `Order` is called "COMPOSITION".
            print("Quantity: {}".format(quantity))
            print("----------------------")
            
        print("Delivery Speed: {}".format(self.delivery_speed))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Delivery Charge: {}".format(Order.delivery_charges[self.delivery_speed]))    #"`Order.delivery_charges`[self.delivery_speed]" <==== accessing class attribute `delivery_charges`
    
    def display_order_bill(self):
        total_bill = 0
        print("------Total Bill---------")
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
            print("{}: Rs.{}".format(product.name, product.price))
        print("Total Bill: Rs.{}".format(total_bill))
     
tv = ElectronicItem("tv", 40000, 35000, 4.9, 24)
keyboard = ElectronicItem("Logitech Keyboard", 1000, 759, 4.2, 12)
mouse = ElectronicItem("Logitech Mouse", 500, 399, 3.9, 12)

flour = GroceryItem("Wheet flour", 100, 90, 4.3, "29/09/2023")
milk = GroceryItem("Amul Milk", 40, 35, 4.4, "30/03/2023")

order = Order("prime_members", "Hyderabad")
order.add_item(milk,3)
order.add_item(tv,1)

order.display_order_details()
order.display_order_bill()




