class Meal:
    def __init__(self, food_name, protein_g, carbs_g, is_hight_protein = False):
        self.food_name = food_name
        self.protein_g = protein_g
        self.carbs_g = carbs_g
        self.is_hight_protein = is_hight_protein
    def check_protein_level(self):
        if self.protein_g >= 20:
            self.is_hight_protein = True
            
Breakfast = Meal("Cafe Latte", 10, 200 )
Dinner = Meal("Chicken beast", 40, 187 )
Lunch = Meal("Cesar Salad", 27, 456 )
daily_list = [ Breakfast, Dinner, Lunch]

for meals in daily_list:
    meals.check_protein_level()
    print(f"{meals.food_name}, {meals.is_hight_protein}")
