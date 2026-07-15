class LoanApplicaiton:
    def __init__(self, client_name,net_income,monthly_installment, status="Feldolgozás alatt"):
        self.client_name = client_name
        self.net_income = net_income
        self.monthly_installment= monthly_installment
        self.status = status
        
    def evalute_jtm(self):
            if self.monthly_installment > (self.net_income * 0.5):
                self.status = " Elutasítva , Rejected"
            else:
                self.status = " Jóváhagyva , Accepted"
Dia = LoanApplicaiton("Dia", 800000,200000)
Ildikó = LoanApplicaiton("Ildikó", 400000,250000)
    
            
applications = [Dia,Ildikó ]
    
for app in applications:
    app.evalute_jtm()
    print(f"{app.client_name}, {app.status}")
        
