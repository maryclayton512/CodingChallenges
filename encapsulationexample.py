
#Name: Mary Clayton
#Date: 7/12/2022
#Purpose: Discussion 2

#make class named coffeeMachine
class coffeeMachine:
    #set self to coffee and cup
    def __init__(self, newCoffee, newCup):
        self._Coffee = newCoffee
        self._Cup = newCup

    #get coffee to self
    def get_coffee(self):
        return self._Coffee
    
    #set coffee and print make coffee
    def set_coffee(self):
        print("Make coffee")

    #get cup to self
    def get_cup(self):
        return self._Cup
    
    #set cup and print pour coffee into cup
    def set_cup(self):
        print("Pour coffee into cup")
    
        
