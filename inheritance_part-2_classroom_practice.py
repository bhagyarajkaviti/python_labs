class Product:      #Super Class
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price
        
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))
    
    def get_deal_price(self):
        return self.deal_price
        
class ElecronicItem(Product):       #Sub Class
    def set_warranty(self, warranty_period):    #Calling `set_warranty` will create attribute `warranty_in_months`
        self.warranty_in_months = warranty_period
        
    def get_warranty(self):
        return self.warranty_in_months
        
    def display_electronic_product_details(self):
        self.display_product_details()      #We can call methods defined in super class from the methods in the sub class. 
        print("Warranty: {} months".format(self.warranty_in_months))

class GroceryItem(Product):
    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date
        
    def get_expiry_date(self):
        return self.expiry_date
        
    def display_grocery_product_details(self):
        self.display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))
        
class Order:
    def __init__(self,delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address
        
    def add_item(self,product, quantity):       # here `product` is an instance to `Order` class. `product` is nothing but an object or an instance of Order class that we create
        self.items_in_cart.append((product, quantity))
    
    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()   #Calling a method  which is in superclass `display_product_details`
            print("Quantity: {}".format(quantity))
            
    def display_order_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity  #`get_deal_price` method inherited from parent class.
            total_bill += price
        print("Total Bill: {}".format(total_bill)) 
    

milk = GroceryItem("Milk", 40, 25, 3.5)
tv = ElecronicItem("TV", 40000, 30000, 4)

order = Order("Prime Dlivery", "Hyderabad")

order.add_item(milk,3)  #here `milk` is an object (instance to the `Order`class) passing as a parameter
order.add_item(tv,1)

order.display_order_details()
order.display_order_bill()