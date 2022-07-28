# has-a relationship between phone number, employee, and customer
class PhoneNumber:
    def __init__(self, newAreaCode, newNumber, newExtension, newPhoneType):
        self.areaCode = newAreaCode
        self.number = newNumber
        self.extension = newExtension
        self.phoneType = newPhoneType

class Person:
    def __init__(self, newName, newLicense, newSocial, newPhone):
        self.name = newName
        self.license = newLicense
        self._social = newSocial
        self.phoneList = []
        self.phoneList.append(newPhone)

class Employee(Person):
    # is-a relationship between person, employee, and customer
    def __init__(self, newEmployeeNum, newHireDate, newName, newLicense, newSocial, newPhone):
        Person.__init__(self, newName, newLicense, newSocial, newPhone)
        self.employeeNum = newEmployeeNum
        self.hireDate = newHireDate

class Customer(Person):
    def __init__(self, newCustomerName, newCreditLimit, newName, newLicense, newSocial, newPhone):
        Person.__init__(self, newName, newLicense, newSocial, newPhone)
        self.customerName = newCustomerName
        self.creditLimit = newCreditLimit


        
    