# ==========================================
# AfriMind Agriculture Knowledge Module
# Version 17.2
# African Agriculture Intelligence
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


# ==========================================
# AGRICULTURE KNOWLEDGE
# ==========================================

agriculture_knowledge = {


    "what is agriculture":
    "Agriculture is the practice of cultivating crops, raising animals, and managing natural resources to produce food and other products.",



    "importance of agriculture":
    "Agriculture provides food, creates employment, supports industries, generates income, and contributes to economic development.",



    "types of agriculture":
    "Types of agriculture include crop farming, livestock keeping, mixed farming, horticulture, and commercial farming.",



    "how to improve farming":
    "Farmers can improve production through quality seeds, proper land preparation, irrigation, fertilizers, pest control, and modern farming technologies.",



    "agriculture challenges":
    "Agriculture challenges include climate change, pests and diseases, lack of capital, poor markets, and limited access to technology.",



    "what is climate smart agriculture":
    "Climate smart agriculture is an approach that increases agricultural productivity while adapting to climate change and reducing environmental impacts."

}



# ==========================================
# AGRICULTURE RESPONSE
# ==========================================

def get_agriculture_answer(question):


    if question in agriculture_knowledge:

        return agriculture_knowledge[question]


    return None