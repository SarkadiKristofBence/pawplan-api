from fastapi import APIRouter
from models import Pet, MealPlan, FoodItem
from utils.planner import generate_meal_plan, get_foods

router = APIRouter()

@router.post("/plan-meal", response_model=MealPlan)
def plan_meal(pet: Pet):
    return generate_meal_plan(pet)

@router.get("/foods", response_model=list[FoodItem])
def list_foods():
    return get_foods()
