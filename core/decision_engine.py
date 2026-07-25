# ==========================================
# AfriMind AI Decision Engine
# Version 17.0
# Problem Analysis and Solution Planning
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


# ==========================================
# ANALYZE PROBLEM
# ==========================================

def analyze_problem(problem):

    problem = problem.lower()



    # Business problems

    if "business" in problem or "biashara" in problem:

        return {
            "category": "Business",
            "analysis": "The problem may be related to management, customers, marketing, or finance.",
            "solutions": [
                "Analyze your customers",
                "Improve marketing strategies",
                "Control expenses",
                "Create a business plan"
            ]
        }



    # Agriculture problems

    if "farm" in problem or "agriculture" in problem or "kilimo" in problem:

        return {
            "category": "Agriculture",
            "analysis": "The problem may involve farming methods, climate, markets, or resources.",
            "solutions": [
                "Identify the farming challenge",
                "Improve production methods",
                "Use better technology",
                "Find reliable markets"
            ]
        }



    # Education problems

    if "education" in problem or "school" in problem:

        return {
            "category": "Education",
            "analysis": "The problem may involve learning resources, skills, or access to education.",
            "solutions": [
                "Identify learning needs",
                "Develop skills",
                "Use available learning resources"
            ]
        }



    # General problem solving

    return {
        "category": "General",
        "analysis": "The problem requires further analysis before providing a solution.",
        "solutions": [
            "Understand the problem",
            "Identify possible causes",
            "Develop solutions",
            "Take action and evaluate results"
        ]
    }



# ==========================================
# GENERATE DECISION RESPONSE
# ==========================================

def make_decision(problem):


    result = analyze_problem(
        problem
    )


    response = f"""
Category: {result['category']}

Analysis:
{result['analysis']}

Recommended Steps:
"""


    for step in result["solutions"]:

        response += f"- {step}\n"


    return response