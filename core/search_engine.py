# ==========================================
# AfriMind AI Search Engine
# Version 19.0
# Internet Knowledge Bridge
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import urllib.request
import urllib.parse
import json



# ==========================================
# SIMPLE WEB SEARCH
# ==========================================

def search_web(question):

    try:

        query = urllib.parse.quote(
            question
        )


        url = (
            "https://api.duckduckgo.com/"
            f"?q={query}&format=json"
        )


        response = urllib.request.urlopen(
            url,
            timeout=5
        )


        data = json.loads(
            response.read()
        )


        answer = data.get(
            "AbstractText"
        )


        if answer:

            return answer


        related = data.get(
            "RelatedTopics"
        )


        if related:

            if len(related) > 0:

                if "Text" in related[0]:

                    return related[0]["Text"]


        return None


    except Exception:


        return None



# ==========================================
# SEARCH RESPONSE
# ==========================================

def get_search_answer(question):


    answer = search_web(
        question
    )


    if answer:

        return answer


    return None