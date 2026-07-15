class BankAccount:
    def __init__(self, client_name, account_number, balance = 0, is_active = True):
        self.client_name = client_name
        self.account_number = account_number
        self.balance = balance
        self.is_active = is_active
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if self.is_active == True and self.balance >= amount:
            self.balance =  self.balance - amount
        else:
            print("Nincs elég fedezeted")
            
    def print_statement(self):
        print(f"{self.client_name}, {self.account_number},{self.balance}")
        
        
Normal = BankAccount("Normal", 123456)
Szabalyszego = BankAccount( "Alma", 3,is_active=False )

Normal.withdraw(1)
Normal.deposit(1)
Normal.print_statement()

Szabalyszego.withdraw(1)
Szabalyszego.deposit(21)
Szabalyszego.print_statement()