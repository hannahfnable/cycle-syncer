
def generate_timetable(phase: PhaseType):
    timetable = Timetable()
    generate_activities = generate_activities(phase)
    timetable.set_activities(generate_activities)
    return timetable
           
def generate_activities(phase: PhaseType):
    mealPlan = generate_meal_plan(phase)
    exercise = suggest_exercise(phase)
    social = suggest_social_activity(phase)
    wellbeing = suggest_wellbeing_activity(PhaseType.menstruation)
    productivity = suggest_productivity_activity(PhaseType.menstruation)
    rest = suggest_rest_activity(PhaseType.menstruation)
    hobby = suggest_hobby_activity(PhaseType.menstruation)
    activities = [mealPlan, exercise, social, wellbeing, productivity, rest, hobby]
    return activities
