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
    def __init__(self, name, price, deal_price, ratings, warranty_period):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_period
    
    #def set_warranty(self, warranty_period):    #Calling `set_warranty` will create attribute `warranty_in_months`
    #    self.warranty_in_months = warranty_period
        
    #def get_warranty(self):
    #    return self.warranty_in_months
        
    def display_product_details(self):  #<==== overriding:Name the sub class method as same as the method name in the super class method. 
    #The sub class method will override the super class method
        super().display_product_details()      #`super()` allows us to call methods of the super class `Product` from the sub class `ElecronicItem`
        print("Warranty: {} months".format(self.warranty_in_months))



    


tv = ElecronicItem("TV", 40000, 30000, 4, 24)   #passing `warranty_period` argument value as 24

tv.display_product_details()



