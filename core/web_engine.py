# ==========================================
# AfriMind AI Web Intelligence Engine
# Version 19.0
# Internet Search Foundation
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import urllib.request
import urllib.parse
import json



# ==========================================
# SEARCH INTERNET
# ==========================================

def search_web(question):

    try:

        query = urllib.parse.quote(question)


        url = (
            "https://api.duckduckgo.com/"
            "?q="
            + query
            +
            "&format=json"
        )


        response = urllib.request.urlopen(
            url,
            timeout=5
        )


        data = json.loads(
            response.read()
        )


        # Abstract answer

        if data.get("AbstractText"):

            return data["AbstractText"]



        # Related topics

        topics = data.get(
            "RelatedTopics",
            []
        )


        for item in topics:

            if isinstance(item, dict):

                if "Text" in item:

                    return item["Text"]



        return None



    except Exception:


        return None



# ==========================================
# AFRIMIND WEB ANSWER
# ==========================================

def get_web_answer(question):


    answer = search_web(
        question
    )


    if answer:


        return (
            "I searched the internet and found this:\n\n"
            +
            answer
        )


    return None