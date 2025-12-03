

class Weekly_Meal_Plan(self):
    def __init__(self, phase: PhaseType):
        self.phase = phase
        self.meals = self.generate_meal_plan(phase)

    def generate_meal_plan(self, phase: PhaseType):
        switch (phase):
            case PhaseType.menstruation:
                return 

    def food_list(self):
        with open('phases.json') as f:
            data = json.load(f)
        return data[self.phase.value]['foods']