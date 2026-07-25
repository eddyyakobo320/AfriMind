# ==========================================
# AfriMind Language Engine v28.0
# ==========================================

import re


def clean_text(text):

    return re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text.lower()
    ).strip()



def detect_topic(question):

    q = clean_text(question)


    topics = {

        "agriculture": [
            "agriculture",
            "farming",
            "farmer",
            "crops",
            "livestock"
        ],

        "artificial intelligence": [
            "ai",
            "artificial intelligence",
            "machine learning"
        ],

        "cybersecurity": [
            "cyber",
            "security",
            "hacking"
        ],

        "community development": [
            "community",
            "development"
        ]

    }


    for topic, words in topics.items():

        for word in words:

            if word in q:
                return topic


    return None