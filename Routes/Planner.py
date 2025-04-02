from fastapi import APIRouter
from models import Pet, MealPlan
from utils.planner import generate_meal_plan

router = APIRouter()

@router.post("/plan-meal", response_model=MealPlan)
def plan_meal(pet: Pet):
    return generate_meal_plan(pet)
