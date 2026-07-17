class Transaction:
    def __init__(self, vendor_name, amount, status = " Pedding"):
        self.vendor_name = vendor_name
        self.amount = amount
        self.status = status

class SecuritySystem:
    def __init__(self, system_name):
        self.system_name = system_name
        self.blocked_list = []
        
    def scan_payment(self, payment):
        if payment.amount >10000:
            self.blocked_list.append(payment)
        else:
            self.status = "Payment was Succesfully"
            
    def show_alerts(self):
        print(f"Warning!, The {self.system_name} blocked these scam payments ")
        for block in self.blocked_list:
            print(f"{block.vendor_name}, {block.amount}")
            

Morning = Transaction("Cofee Shop", 1500)
Daily_routine = Transaction("Lild", 8500)
Scam = Transaction("About You", 2500000)

my_firewall = SecuritySystem("Mark_NetBank")
my_firewall.scan_payment(Morning)
my_firewall.scan_payment(Daily_routine)
my_firewall.scan_payment(Scam)
my_firewall.show_alerts()