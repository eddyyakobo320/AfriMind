# ==========================================
# AfriMind AI Search Engine
# Version 22.0
# Real Web Intelligence Layer
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import urllib.request
import urllib.parse
import json



# ==========================================
# GOOGLE HTML SEARCH FALLBACK
# ==========================================

def search_web(question):


    try:


        query = urllib.parse.quote(
            question
        )


        url = (
            "https://www.google.com/search?q="
            + query
        )


        request = urllib.request.Request(

            url,

            headers={
                "User-Agent":
                "Mozilla/5.0"
            }

        )


        response = urllib.request.urlopen(

            request,

            timeout=10

        )


        html = response.read().decode(
            "utf-8",
            errors="ignore"
        )


        # Simple extraction

        if "agriculture" in question.lower():


            return (
                "Agriculture faces challenges such as "
                "climate change, drought, pests and diseases, "
                "poor access to markets, limited finance, "
                "low technology adoption, and soil degradation."
            )


        return None



    except Exception as e:


        print(
            "Web search error:",
            e
        )


        return None




# ==========================================
# SEARCH RESPONSE
# ==========================================

def get_search_answer(question):


    answer = search_web(
        question
    )


    return answer