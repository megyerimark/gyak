class Meal:
    def __init__(self, food_name, protein_g, carbs_g, is_hight_protein = False):
        self.food_name = food_name
        self.protein_g = protein_g
        self.carbs_g = carbs_g
        self.is_hight_protein = is_hight_protein
    def check_protein_level(self):
        if self.protein_g >= 20:
            self.is_hight_protein = True
class DietApp:
    def __init__(self, user_name):
        self.user_name = user_name
        self.daily_meals = []
    def add_meals(self, meal_item):
        self.daily_meals.append(meal_item)
        
        
        
    def print_summary(self):
        print({f"Napi összesítő - {self.user_name} Fiókja"})
        for m in self.daily_meals:
            print(f"{m.food_name}, {m.protein_g}")

daily_meals = []
Breakfast = Meal("Cafe Latte", 10, 200 )
Dinner = Meal("Chicken beast", 40, 187 )
Lunch = Meal("Cesar Salad", 27, 456 )            
# daily_list = [ Breakfast, Dinner, Lunch]     
    
my_tracker = DietApp("Márk")
my_tracker.add_meals(Breakfast)
my_tracker.add_meals(Dinner)
my_tracker.add_meals(Lunch)
my_tracker.print_summary()