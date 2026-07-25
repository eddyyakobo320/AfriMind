# ==========================================
# AfriMind AI Module Manager
# Version 17.4
# Automatic Knowledge Module Loader
# Building Intelligence for Africa
# Created by Edward Yakobo Mganga
# ==========================================


import os
import importlib



# ==========================================
# MODULE DIRECTORY
# ==========================================

MODULE_FOLDER = "modules"



# ==========================================
# LOAD ALL MODULES
# ==========================================

def load_modules():

    modules = []


    if not os.path.exists(MODULE_FOLDER):

        return modules



    for file in os.listdir(MODULE_FOLDER):


        if file.endswith(".py") and file != "__init__.py":


            module_name = (
                file
                .replace(".py", "")
            )


            try:

                module = importlib.import_module(
                    f"modules.{module_name}"
                )


                modules.append(
                    module
                )


            except Exception:

                pass



    return modules



# ==========================================
# SEARCH MODULE ANSWERS
# ==========================================

def get_module_answer(question):


    modules = load_modules()



    for module in modules:


        for function_name in dir(module):


            if function_name.startswith(
                "get_"
            ) and function_name.endswith(
                "_answer"
            ):


                function = getattr(
                    module,
                    function_name
                )


                try:

                    answer = function(
                        question
                    )


                    if answer:

                        return answer


                except Exception:

                    continue



    return None