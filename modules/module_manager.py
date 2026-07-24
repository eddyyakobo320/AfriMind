# ==========================================
# AfriMind Module Manager
# Version 2.0
# Intelligent Module Loading System
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


from modules.agriculture import agriculture_knowledge
from modules.business import business_knowledge
from modules.health import health_knowledge



# ==========================
# REGISTER MODULES
# ==========================

modules = {

    "agriculture": agriculture_knowledge,

    "business": business_knowledge,

    "health": health_knowledge

}



# ==========================
# COMBINE ALL KNOWLEDGE
# ==========================

def get_all_module_knowledge():

    combined_knowledge = {}


    for module in modules.values():

        combined_knowledge.update(
            module
        )


    return combined_knowledge



# ==========================
# SEARCH MODULES
# ==========================

def search_modules(question):


    for module in modules.values():


        if question in module:

            return module[question]


    return None