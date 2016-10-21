class Stock(object):
    
    stock_objects = []
    
    def __init__(self, model, item, make, price, quantity):
        self.model = model
        self.item = item
        self.make = make
        self.price = price
        self.quantity = quantity
    
    def getModel(self):
        return self.model
        
    def getItem(self):
        return self.item
    
    def getMake(self):
        return self.make
    
    def getPrice(self):
        return self.price
    
    def getQuantity(self):
        return self.quantity

    #def __str__(self):
    #    return "%s is a %s from %s. The price is %s with %s in stock." % (self.model, self.item, self.make, self.price, self.quantity)
    
class SumStock(Stock):
    
    def __init__(self, name, value, total_value, valuecalc, totalcalc):
        Stock.__init__(self, name, "SumStock")
        self.value = value
        self.total_value = total_value
        self.valuecalc = valuecalc
        self.totalcalc = totalcalc
        
    def getValue(self):
        # put code here...
        return
    
    def getTotal_Value(self):
        # put code here...
        return self.total_value
    
    def valueCalc(self, name):
        # put code here...
        return self.valuecalc
        
    def totalCalc(self):
        # put code here...
        return self.totalcalc
    
class UserInput(object):
    
    def __init__(self, name):
        self.name = name
        
    def getInput(self):
        print ("1: Add Item\n2: Get Item Quantity\n3: Item In Stock Value\n4: Inventory Total\n5: Exit")
        choice = int(raw_input('Select an option: '))
        if choice == 1:
            print ('Add Item')
            enter_model = raw_input('Enter Model: ')
            enter_item = raw_input('Enter Type: ')
            enter_make = raw_input('Enter Make: ')
            enter_price = raw_input('Enter Price: ')
            enter_quantity0 = raw_input('Enter Quantity: ')
            (enter_model) = Stock(enter_model, enter_item, enter_make, enter_price, enter_quantity0)
            return 
        elif (choice == 2):
            print ('Get Item Quantity')
            enter_quantity1 = raw_input('Enter Model: ')
            Stock.getQuantity(enter_quantity1)
        elif (choice == 3):
            print ('Item In Stock Value')
            enter_model_total = raw_input('Enter Model: ')
            SumStock.getValue(enter_model_total)
        elif (choice == 4):
            print ('Inventory Total')
            SumStock.getTotal_Value()
        elif (choice == 5):
            print ('Exiting...')               
        else:
            print ('Invalid Entry')
        return choice    

startit = UserInput('startit')
start_program = startit.getInput()
#while start_program != 5:
#    continue
        
print 'Done'