

import json
from enums.phase_type import PhaseType


class Weekly_Meal_Plan:
    def __init__(self, phase: PhaseType):
        self.phase = phase
        self.meals = self.generate_meal_plan(phase)

    def generate_meal_plan(self, phase: PhaseType):
        match (phase):
            case PhaseType.menstruation:
                return 

    def getFoodList(self):
        with open('phases.json') as f:
            data = json.load(f)
        foodData = data[self.phase.value]
        return foodData
    
    def getShoppingList(self):
        foodList = self.getFoodList()
        shoppingList = {}
        for meal in foodList['meals']:
            for ingredient in meal['ingredients']:
                name = ingredient['name']
                quantity = ingredient['quantity']
                if name in shoppingList:
                    shoppingList[name] += quantity
                else:
                    shoppingList[name] = quantity
        return shoppingList