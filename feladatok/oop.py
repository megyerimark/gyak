class Client:
    def __init__(self, name, age, income, loan_amout, status = " Pedding"):
        self.name = name
        self.age = age
        self.income = income
        self.loan_amout = loan_amout
        self.status = status
        
    def evaluate_risk(self):
        if self.age <= 18:
            self.status = " Rejected"
        if self.loan_amout > self.income*10:
            self.status =" Hight Risk"
        else:
            self.status = " Approved"
    def print_decision(self):
        print(f"{self.name}, {self.loan_amout}, {self.status}")
        
Matyi = Client("Matyi", 17, 340, 34000000,)
ildi = Client("Ildi", 34, 3400000, 34000,)
Máté = Client("Máté", 44, 34, 34000000,)

Matyi.evaluate_risk()
ildi.evaluate_risk()
Máté.evaluate_risk()

Matyi.print_decision()
ildi.print_decision()
Máté.print_decision()
    