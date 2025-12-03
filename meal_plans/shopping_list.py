

class Shopping_List:
    def __init__(self, phase: PhaseType):
        self.fresh_items = self.generate_shopping_list(phase)
        self.optional_items = self.get_stored_items(phase)

    def generate_shopping_list(self, phase: PhaseType):
        foods.foods.filter(phase=phase)