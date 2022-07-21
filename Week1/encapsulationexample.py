
#Name: Mary Clayton
#Date: 7/12/2022
#Purpose: Discussion 2

#make class named coffeeMachine
class coffeeMachine:
#INPUT
    #set self to coffee and cup
    def __init__(self, newCoffee, newCup):
        self._coffee = newCoffee
        self._cup = newCup

    #get coffee to self
    def get_coffee(self):
        return self.coffee
    
    #set coffee and print make coffee
    def set_coffee(self):
        print("Make coffee")

    #get cup to self
    def get_cup(self):
        return self.cup
    
    #set cup and print pour coffee into cup
    def set_cup(self):
        print("Pour coffee into cup")
#OUTPUT
cm = coffeeMachine("expresso", "red mug")
print(cm.get_coffee())
print(cm.get_cup())
        
