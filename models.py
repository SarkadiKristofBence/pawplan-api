from pydantic import BaseModel
from typing import List, Optional

class Pet(BaseModel):
    name: str
    age: float  # in years
    species: str  # dog or cat
    breed: Optional[str] = None
    weight: float  # in kg
    activity_level: str  # low, medium, high
    health_issues: Optional[List[str]] = []

class FoodItem(BaseModel):
    name: str
    protein: float  # g per 100g
    fat: float      # g per 100g
    carbs: float    # g per 100g
    calories: float # kcal per 100g

class MealPlan(BaseModel):
    meals: List[FoodItem]
    total_calories: float
    total_protein: float
    total_fat: float
    total_carbs: float
