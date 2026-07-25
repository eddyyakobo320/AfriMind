# ==========================================
# AfriMind Health Intelligence Module
# Version 17.3
# Community Health Knowledge
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


# ==========================================
# HEALTH KNOWLEDGE BASE
# ==========================================

health_knowledge = {


    "what is health":
    "Health is a state of physical, mental, and social well-being that enables people to live productive lives.",



    "importance of health":
    "Good health improves quality of life, increases productivity, supports learning, and helps communities develop.",



    "what is disease prevention":
    "Disease prevention involves actions taken to reduce the risk of diseases through healthy behaviours, vaccination, sanitation, and early awareness.",



    "what is nutrition":
    "Nutrition is the process of obtaining and using nutrients from food to support growth, energy, and body functions.",



    "healthy lifestyle":
    "A healthy lifestyle includes balanced nutrition, regular physical activity, enough rest, hygiene, and avoiding harmful behaviours.",



    "importance of clean water":
    "Clean water is important for preventing waterborne diseases and maintaining good health.",



    "community health":
    "Community health focuses on improving the health and well-being of people through awareness, prevention, and collective action."

}



# ==========================================
# HEALTH RESPONSE
# ==========================================

def get_health_answer(question):


    if question in health_knowledge:

        return health_knowledge[question]


    return None