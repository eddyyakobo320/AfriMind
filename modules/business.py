# ==========================================
# AfriMind Business Knowledge Module
# Version 17.1
# African Business Intelligence
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================



# ==========================================
# BUSINESS KNOWLEDGE
# ==========================================

business_knowledge = {


    "what is business":
    "Business is an activity of producing, buying, or selling goods and services to create value and generate income.",



    "what is entrepreneurship":
    "Entrepreneurship is the process of creating, developing, and managing a business opportunity.",



    "how to start a business":
    "To start a business you need an idea, market research, capital, a business plan, customers, and good management.",



    "importance of business":
    "Business creates employment, generates income, provides goods and services, and contributes to economic development.",



    "business challenges":
    "Common business challenges include lack of capital, poor marketing, competition, financial management problems, and changing customer needs.",



    "how to improve business":
    "Improve your business by understanding customers, increasing marketing, controlling costs, improving quality, and using technology."

}



# ==========================================
# BUSINESS RESPONSE
# ==========================================

def get_business_answer(question):


    if question in business_knowledge:

        return business_knowledge[question]


    return None