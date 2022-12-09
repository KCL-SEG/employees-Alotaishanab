"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    FIXED_BONUS = 'fixed bonus'
    CONTRACT_BONUS = 'contract bonus'

    HOURLY = 'hourly'
    SALARY = 'salary'

    def __init__(self, name, wage, contract_type, hours=None, commission: dict = None):
        self.name = name
        self.contract_type = contract_type
        self.commission = commission
        self.wage = wage
        self.hours = hours
        try:
            self.commission_type = self.commission['type']
        except TypeError:
            self.commission_type = None

    def get_commission(self):
        if self.commission_type == self.FIXED_BONUS:
            return self.commission['bonus']
        elif self.commission_type == self.CONTRACT_BONUS:
            return self.commission['rate'] * self.commission['number_of_contract']
        else:
            return 0

    def get_pay(self):
        if self.contract_type == self.HOURLY:
            return self.get_commission() + (self.wage * self.hours)
        else:
            return self.get_commission() + self.wage

    def __str__(self):
        if self.contract_type == self.SALARY and self.commission_type is None:
            return f'{self.name} works on a monthly salary of {self.wage}.  Their total pay is {self.get_pay()}.'
        elif self.contract_type == self.HOURLY and self.commission_type is None:
            return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour.  Their total pay is {self.get_pay()}.'
        elif self.contract_type == self.SALARY and self.commission_type == self.CONTRACT_BONUS:
            return f'{self.name} works on a monthly salary of {self.wage} and receives a commission for {self.commission["number_of_contract"]} contract(s) at {self.commission["rate"]}/contract.  Their total pay is {self.get_pay()}.'
        elif self.contract_type == self.HOURLY and self.commission_type == self.CONTRACT_BONUS:
            return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.commission["number_of_contract"]} contract(s) at {self.commission["rate"]}/contract.  Their total pay is {self.get_pay()}.'
        elif self.contract_type == self.SALARY and self.commission_type == self.FIXED_BONUS:

            return f'{self.name} works on a monthly salary of {self.wage} and receives a bonus commission of {self.get_commission()}.  Their total pay is {self.get_pay()}.'
        elif self.contract_type == self.HOURLY and self.commission_type == self.FIXED_BONUS:

            return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.get_commission()}.  Their total pay is {self.get_pay()}.'




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', wage=4000, contract_type='salary')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', wage=25, contract_type='hourly', hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', wage=3000, contract_type='salary', commission={'number_of_contract': 4, 'rate': 200, 'type': 'contract bonus'})

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', wage=25, contract_type='hourly', hours=150, commission={'number_of_contract': 3, 'rate': 220, 'type': 'contract bonus'})

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', wage=2000, contract_type='salary', commission={'type': 'fixed bonus', 'bonus': 1500})

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', wage=30, contract_type='hourly', hours=120, commission={'type': 'fixed bonus', 'bonus': 600})
