class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        # TODO: Declare purchase_price attribute
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print("Car's Information:")
        print("Model year:", self.model_year)
        print("Purchase price:", self.purchase_price) 
        print("Current Value:", self.current_value)
            
if __name__ == "__main__":    
    year = int(input("Enter Car's year: ")) 
    price = int(input("Enter Car's price: "))
    current_year = int(input("Enter current year: "))
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()

    # try:
    #     my_car.print_info()
    # except Exception as E:
    #     print(E)