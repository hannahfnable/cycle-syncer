
def suggest_exercise(phase: PhaseType) -> str:
    match phase:
        case PhaseType.MENSTRUATION:
            return "Light yoga and stretching"
        case PhaseType.FOLLICULAR:
            return "Cardio and strength training"
        case PhaseType.OVULATION:
            return "High-intensity interval training (HIIT)"
        case PhaseType.LUTEAL:
            return "Moderate cardio and pilates"
    return "Rest or light activity"

def suggest_wellbeing_activity(phase: PhaseType) -> str:
    match phase:
        case PhaseType.MENSTRUATION:
            return "Aromatherapy and warm baths"
        case PhaseType.FOLLICULAR:
            return "Outdoor activities and socializing"
        case PhaseType.OVULATION:
            return "Creative hobbies and dance"
        case PhaseType.LUTEAL:
            return "Journaling and mindfulness practices"
    return "Self-care and pampering"

def suggest_social_activity(phase: PhaseType) -> str:
    match phase:
        case PhaseType.MENSTRUATION:
            return "Small gatherings with close friends"
        case PhaseType.FOLLICULAR:
            return "Group sports or team activities"
        case PhaseType.OVULATION:
            return "Parties or social events"
        case PhaseType.LUTEAL:
            return "Quiet dinners or movie nights"
    return "Connect with loved ones"

def suggest_productivity_activity(phase: PhaseType) -> str:
    match phase:
        case PhaseType.MENSTRUATION:
            return "Planning and organizing tasks"
        case PhaseType.FOLLICULAR:
            return "Brainstorming and creative projects"
        case PhaseType.OVULATION:
            return "Networking and collaborative work"
        case PhaseType.LUTEAL:
            return "Detail-oriented tasks and reviews"
    return "Focus on your goals"
    
def suggest_hobby_activity(phase: PhaseType) -> str:
    match phase:
        case PhaseType.MENSTRUATION:
            return "Reading or knitting"
        case PhaseType.FOLLICULAR:
            return "Gardening or painting"
        case PhaseType.OVULATION:
            return "Dancing or playing musical instruments"
        case PhaseType.LUTEAL:
            return "Cooking or puzzles"
    return "Engage in your favorite hobbies"