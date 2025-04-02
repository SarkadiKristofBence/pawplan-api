from models import Pet, MealPlan, FoodItem

# Sample food database (can later be moved to JSON)
food_db = [
    FoodItem(name="Chicken Breast", protein=31.0, fat=3.6, carbs=0.0, calories=165),
    FoodItem(name="Beef", protein=26.0, fat=15.0, carbs=0.0, calories=250),
    FoodItem(name="Rice", protein=2.7, fat=0.3, carbs=28.0, calories=130),
    FoodItem(name="Salmon", protein=25.0, fat=14.0, carbs=0.0, calories=208)
]

def generate_meal_plan(pet: Pet) -> MealPlan:
    # Estimate daily calorie needs (simplified)
    weight_factor = 30 if pet.species.lower() == "dog" else 40
    activity_multiplier = {"low": 1.2, "medium": 1.5, "high": 1.8}.get(pet.activity_level, 1.2)
    calories_needed = pet.weight * weight_factor * activity_multiplier

    # Simplified meal generation
    meals = [food_db[0], food_db[2]]  # Chicken + Rice as a basic plan
    total_calories = sum(f.calories for f in meals)
    total_protein = sum(f.protein for f in meals)
    total_fat = sum(f.fat for f in meals)
    total_carbs = sum(f.carbs for f in meals)

    return MealPlan(
        meals=meals,
        total_calories=total_calories,
        total_protein=total_protein,
        total_fat=total_fat,
        total_carbs=total_carbs
    )

def get_foods() -> list[FoodItem]:
    return food_db
