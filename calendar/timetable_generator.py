
from calendar.timetable import Timetable
from meal_plans.meal_planner import generate_meal_plan
from enums.phase_type import PhaseType
from activity_generators import (
    suggest_exercise,
    suggest_social_activity,
    suggest_wellbeing_activity,
    suggest_productivity_activity,
    suggest_rest_activity,
    suggest_hobby_activity
)


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
