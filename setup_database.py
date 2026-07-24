# ==========================================
# AfriMind Database Setup
# Version 3.0
# Created by Edward Yakobo Mganga
# ==========================================

from database import create_table, add_knowledge


# Create database table
create_table()


# Add initial knowledge
add_knowledge(
    "what is afrimind",
    "AfriMind is an Artificial Intelligence project built to provide knowledge and solutions for Africa."
)

add_knowledge(
    "what is python",
    "Python is a programming language used to build software, artificial intelligence, and many other applications."
)

add_knowledge(
    "who created you",
    "I was created by Edward Yakobo Mganga."
)

add_knowledge(
    "what is cybersecurity",
    "Cybersecurity is the practice of protecting computers, networks, and information from cyber attacks."
)

add_knowledge(
    "what is community development",
    "Community development is a process where people work together to improve their social, economic, and environmental conditions."
)

add_knowledge(
    "what is tanzania",
    "Tanzania is a country in East Africa."
)


print("AfriMind database setup completed successfully!")
