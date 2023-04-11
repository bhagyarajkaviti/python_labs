class Cart:
    flat_discount = 0
    min_bill = 100
    def __init__(self):
       self.items = {}
    def add_item(self, item_name,quantity):
       self.items[item_name] = quantity
       self.display_items() # calling instance method inside the class
    def display_items(self):
       print(self.items)
    def print_min_bill(self):
        print(Cart.min_bill)    #Accessing `class-attribute` inside the class
    
    @classmethod#===> Decorator: It marks the method below it as `class method`
    def update_flat_discount(cls, updated_flat_discount):
        cls.flat_discount = updated_flat_discount
    
    @classmethod        #Class Method
    def increase_flat_discount(cls,amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount) #calling another class method inside the class method.
        
    @staticmethod   #Static method     
    def greet():    #utility function
        print("Have a great shopping")
       
a = Cart()
b = Cart()
a.add_item("book", 3) #calling instance method outside of the class.
print(a.items)

Cart.min_bill = 200 #Updating the class-attribute value
 
a.print_min_bill()
b.print_min_bill()

Cart.update_flat_discount(25)
print(Cart.flat_discount)

Cart.increase_flat_discount(50)
print(Cart.flat_discount)

Cart.greet()