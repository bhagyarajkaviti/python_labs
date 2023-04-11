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
        
p = Product('laptop', 40000, 25000, 4)
p.display_product_details()
print("\n")

e = ElecronicItem('T.V', 17000, 14000, 4.5)
#e.display_product_details()
e.set_warranty(24)
e.display_electronic_product_details()
print("\t")

g = GroceryItem('Milk', 30, 23, 4.2)
#g.display_product_details()
g.set_expiry_date("24/03/2023")
g.display_grocery_product_details()