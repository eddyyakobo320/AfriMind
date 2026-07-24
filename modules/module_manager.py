# ==========================================
# AfriMind Module Manager
# Version 1.0
# Loads all knowledge modules
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================

from modules.agriculture import agriculture_knowledge
from modules.business import business_knowledge
from modules.health import health_knowledge


# List of all knowledge modules
all_modules = [

    agriculture_knowledge,
    business_knowledge,
    health_knowledge

]