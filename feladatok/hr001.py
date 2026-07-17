class Programmer:
    def __init__(self, name, primary_language, status = " Open to job"):
        self.name = name
        self.primary_language = primary_language
        self.status = status
        
class TechCompany:
    def __init__(self, company_name):
        self.company_name = company_name
        self.hired_developers = []
        
    def interview(self, candidate):
        if candidate.primary_language == "Python":
            candidate.status = " Felvéve"
            self.hired_developers.append(candidate)
        else:
            print("Elutasítva")
            
    
    def show_team(self):
        print(f"A {self.company_name} cég fejlesztői csapata")
        for dev in self.hired_developers:
            print(f"{dev.name}, {dev.primary_language}, {dev.status}")

Python = Programmer("Márk", "Python")
Java = Programmer("Béla", " Java")
C_net = Programmer("Csaba", " C")

my_company = TechCompany("Python ZRT")
my_company.interview(Python)
my_company.interview(Java)
my_company.interview(C_net)
my_company.show_team()